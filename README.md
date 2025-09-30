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

