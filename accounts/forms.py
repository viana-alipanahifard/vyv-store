from django import forms
from .models import User,OtpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
  
    
    class Meta:
        model=User
        fields=('email','phone_number','full_name')
        
        
        def clean_password2(self):
            cd=self.cleaned_data()
            if cd['password1'] and cd['password2'] and cd['password1']!=cd['password2']:
                raise ValidationError('passwords not match')
            return cd['password2']
        
        def save(self,commit=True):
            user=super().save(commit=False)
            user.set_password(self.cleaned_data['password1'])
            if commit:
                user.save()
            return user
        
        
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField(help_text="you can change your password usin <a href=\" ../password/\"> this form</a>.")
    
    class Meta:
        model=User
        fields=('email','phone_number','full_name','password','last_login')
        
        
        
class UserRegistrationForm(forms.Form):
    phone=forms.CharField(max_length=11)
    email=forms.EmailField(max_length=200)
    full_name=forms.CharField(max_length=200,label='full_name')
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists() 
        if user:
            raise ValidationError('this email already exists')
        return email
    
    def clean_phone_number(self):
        phone=self.cleaned_data['phone_number']
        user=User.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('this phone number already exists')
        OtpCode.objects.filter(phone_number=phone).delete()
        return phone
    
    
    
class VerifyCodeForm(forms.Form):
    code=forms.IntegerField()
    
    
class UserLoginForm(forms.Form):
    phone=forms.CharField(max_length=11)
    password=forms.CharField(widget=forms.PasswordInput)
    