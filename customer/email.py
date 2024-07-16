from django.conf import settings
from django.core.mail import send_mail

def emailSend(inputemail,otp):
    try:
        return send_mail( 
            from_email= 'mkcl@23bg.tech',
            subject = 'welcome to GFG world',
            message = f'Hi {inputemail}, is your otp {otp}.',
            recipient_list = [f"{inputemail}"],
            )
    except(LookupError):
        return print(LookupError)
    

