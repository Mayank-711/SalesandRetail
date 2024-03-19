from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def send_email_to_client(email,token):
    subject='This email is for Resetting your password'
    message=f'Please,Click on the link to reset your password http://127.0.0.1:8000/ChangePassword/{token}/'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True