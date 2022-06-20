from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
def my_mail(subject, token, url, to):  
    # subject = "Greetings from Programink"  
    # msg     = "Learn Django at Programink.com"  
    # to      = "hello@programink.com"  
    html = render_to_string('mail_content.html', {"title": subject, "token": token, "url": url})
    res = send_mail(subject=subject,message="Hello Con ba bay", html_message = html,from_email= settings.EMAIL_HOST_USER, recipient_list=[to, ])  
    if(res == 1):  
        msg = "Mail Sent Successfully."  
    else:  
        msg = "Mail Sending Failed."  
    return msg  