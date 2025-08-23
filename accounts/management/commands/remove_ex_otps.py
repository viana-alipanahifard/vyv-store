from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime,timedelta
import pytz



class Command(BaseCommand):
    help='this command will delete all expierds otp codes'
    
    def handle(self, *args, **options):
        expierd_times=datetime.now(tz=pytz.timezone('Asia/Tehran'))- timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expierd_times).delete()
        self.stdout.write('all expierds otp codes deleted successfully')
        