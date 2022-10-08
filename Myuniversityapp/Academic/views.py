from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contactForm(request):
    return render(request, "contact_form.html")

def contact(request):
    if request.method == "POST":
        name = request.POST["txtName"]
        subject = request.POST["txtSubject"]
        message = request.POST["txtMessage"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER 
        email_para = ["pruebadjango8@gmail.com"]
        send_mail(subject, message, from_email=email_desde, recipient_list=email_para, fail_silently=False)
        return render(request, "successfulContact.html")
    return render(request, "contact_form.html")



    
    