
from  django.conf import settings
from django.core.mail import EmailMultiAlternatives

def run():
  subject = "I send to y a file"
  text = "how are you my friends"
  From_mail = settings.EMAIL_HOST_USER
  To_mail= ['mizanmd92782@gmail.com']

  msg= EmailMultiAlternatives(
    subject,text,From_mail,To_mail
  )


  # read  html file
  html_path = settings.BASE_DIR / 'templates' / 'home.html'



  with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

  msg.attach_alternative(html_content, "text/html")

  msg.send()
