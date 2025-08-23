from celery import shared_task
from accounts.models import OtpCode
from datetime import datetime,timedelta
import pytz

@shared_task
def remove_ex_otp_codes():
        expierd_times=datetime.now(tz=pytz.timezone('Asia/Tehran'))- timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expierd_times).delete()