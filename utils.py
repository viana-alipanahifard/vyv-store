from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin




def send_otp_code(phone_number,code):
    try:
        api=KavenegarAPI('316565596B4A47384A68322F4A3069506A45754B3745655146495842434A496E41657A6151774E446C4')
        params={
            'sender':'2000660110',
            'receptor':phone_number,
            'message':f'your code is ::  {code}',
        }
    
        response = api.sms_send( params) 
        print(response)
        
    except APIException as e: 
         print(e)
    except HTTPException as e: 
         print(e)
         
class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return  self.request.user.is_authenticated and self.request.user.is_admin
