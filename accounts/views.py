from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegistrationForm,VerifyCodeForm,UserLoginForm
import random
from utils import *
from . models import OtpCode,User
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(View):
    form_class=UserRegistrationForm
    templates_name='accounts/register.html'
    
    def get(self,request):
        form=self.form_class
        return render(request,self.templates_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            random_code=random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone'],random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'],code=random_code)
            request.session['user_registeration_info']={
                'phone_number':form.cleaned_data['phone'],
                'email':form.cleaned_data['email'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password'],
            }
            messages.success(request,'we send you a code','success')
            return redirect('accounts:verify_code')
        return render(request,self.templates_name,{'form':form})
    
    
    
class UserRegisterVerifyCode(View):
    form_class=VerifyCodeForm
    
    def get(self,request):
        form=self.form_class
        return render(request,'accounts/verify.html',{'form':form})
    
    
    def post(self,request):
        user_session=request.session['user_registeration_info']
        code_instance=OtpCode.objects.get(phone_number=user_session['phone_number'])
        form=self.form_class(request.POST)
        expiration_time = code_instance.created+timedelta(seconds=120)
    
        if form.is_valid():
            cd=form.cleaned_data
            if timezone.now() > expiration_time:
                code_instance.delete()  
                messages.error(request, 'OTP code has expired. Please request a new one.', 'danger')
                return redirect('accounts:verify_code')
            if cd['code']==code_instance.code:                
                User.objects.create_user(user_session['phone_number'],user_session['email'],user_session['full_name'],user_session['password'])
                code_instance.delete()
                messages.success(request,'you registered successfully.','success')
                return redirect('home:home')
            
            else:
                messages.error(request,'this code is wrong','danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')
        
    

class UserLoginView(View):
    form_class=UserLoginForm
    templates_name='accounts/login.html'
    
    def get(self,request):
        form=self.form_class
        return render(request,self.templates_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,phone_number=cd['phone'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'you logged in successfuly','success')
                return redirect('home:home')
            messages.error(request,'phone or password is wrong', 'warning')
        return render(request,self.templates_name,{'form':form})
    

    
class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'you logged out successfully','success')
        return redirect('home:home')        