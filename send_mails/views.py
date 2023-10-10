from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages


# Create your views here.
def smtp_send_mail(request):
    if request.method == "POST":
        to = request.POST['to']
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER
        
        if not (to and subject and message):
            messages.error(request, "Make sure all fields are entered and valid.")
        
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ["rautsantosh20@gmail.com"])
                messages.success(request, "Mail sent successfully.")
            except BadHeaderError:
                messages.error(request, "Invalid header found.")
        return redirect("/send_mails/send_mail")
        
        
    return render(request, "send_mails/send_mail.html", {})