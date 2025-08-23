from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import User,OtpCode
from django.contrib.auth.models import Group



class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm
    
    
    list_display=['phone_number','email','is_admin']
    list_filter=['is_admin']
    readonly_fields=('last_login',)
    
    fieldsets=(
        
        (None,{'fields' : ('email','phone_number','full_name','password')}),
        ('permissions',{'fields':('is_active','is_superuser','is_admin','last_login','groups','user_permissions')}),

    )
    
    add_fieldsets=(
        
        (None,{'fields':('email','phone_number','full_name','password1','password2' )}), 
    )
    
    
    search_fields=('email','full_name')
    ordering=('full_name',)
    filter_horizontal=('groups','user_permissions')
    
    
    
@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display=['phone_number','code','created']

    

def get_form(self,request,obj=None, **kwargs):
    form=super().get_form(request,obj, **kwargs)
    is_superuser=request.user.is_superuser
    if not is_superuser:
        form.base_fields['is_superuser'].disabled=True
    return form
    


admin.site.register(User,UserAdmin)
