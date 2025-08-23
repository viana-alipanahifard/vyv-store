vVyana-store · Django 4.2

پروژهٔ بک‌اند فروشگاهی با Django برای نمایش مهارت‌ها: URLهای تمیز و امن، OTP پیامکی با کاوه‌نگار، پرداخت زرین‌پال (کد آماده)، ذخیره‌سازی S3-Compatible (ArvanCloud)، و پردازش پس‌زمینه با Celery + RabbitMQ + Celery Beat.

 ویژگی‌ها
- **URLهای تمیز و امن**: namespace + reverse + UUID + تنظیمات امن تولید
- **OTP (Kavenegar)**: ثبت‌نام/ورود با کد یک‌بارمصرف + expire + rate limit
_پرداخت (Zarinpal): درخواست/بازگشت/تأیید با feature flag (sandbox-ready)
- ذخیره‌سازی (S3/ArvanCloud): آپلود مدیا با `django-storages[boto3]`
- پس‌زمینه: Celery worker + RabbitMQ broker + Celery Beat برای زمان‌بندی


## 🚀 شروع سریع (Local)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver






DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://user:pass@localhost:5432/{{db_name}}

# OTP (Kavenegar)
KAVENEGAR_API_KEY=
KAVENEGAR_OTP_TEMPLATE=otp
OTP_EXP_MINUTES=2
OTP_RATE_LIMIT_PER_IP=5

# Zarinpal
ZARINPAL_ENABLED=False
ZARINPAL_MERCHANT_ID=
ZARINPAL_CALLBACK_URL=https://your-domain.com/payment/verify/

# Celery / RabbitMQ
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
CELERY_RESULT_BACKEND=rpc://
CELERY_TIMEZONE=Asia/Tehran

# S3-Compatible (ArvanCloud)
USE_S3=True
AWS_ACCESS_KEY_ID=![Screenshot 2025-08-23 at 19 42 04](https://github.com/user-attachments/assets/c8750296-4567-4c96-a5f9-eaaad7acce73)

AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME={{bucket}}
AWS_S3_REGION_NAME=ir-any
AWS_S3_ENDPOINT_URL=https://s3.ir-thr-at1.arvanstorage.com
AWS_S3_CUSTOM_DOMAIN=
<img width="1512" height="982" alt="مشخصات نهایی-" src="https://github.com/user-attachments/assets/939cf8e1-9fc4-40c3-bb3e-cbf9fb22f828" />
<img width="1512" height="982" alt="باکت ها" src="https://github.com/user-attachments/assets/ec30a814-7043-4b97-a01c-243b4d67fd75" />
<img width="1512" height="982" alt="صفحه ی ثبت نام (رجیستر" src="https://github.com/user-attachments/assets/a3902a26-9190-4ac6-a2d8-75acf7b9b645" />
<img width="1512" height="982" alt="صفحه ی ثبت نام (رجیستر" src="https://github.com/user-attachments/assets/c5748f7f-66dc-46b9-bc89-d4d22d52b4c2" />
