from django.core.mail import send_mail
from django.conf import settings



def run():
    subject = "Django থেকে শুভেচ্ছা!"
    message = '''তুমি সফলভাবে Django SMTP সেটআপ করেছো 

     i hope you are doing well 

     i miss you,

     its long time,i dont see you, 

     fell free to meet with me when you are free
   
    '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mizanmd92782@gmail.com']

    send_mail(subject, message, email_from, recipient_list)
    return "Email পাঠানো সম্পন্ন "