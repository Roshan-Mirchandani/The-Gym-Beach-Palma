from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages  # To show success/error messages
from django.http import HttpResponseRedirect 
import json

# Create your views here.

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('query')
        number = request.POST.get('number')

        subject = f"New Query from {name}"
        full_message = f" Name: {name}\n Email: {email} \n Phone Number: {number}\n \n  {message} \n"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_RECEIVER],
                fail_silently=False
            )

            messages.success(request, 'Your query has been sent successfully!')
            return HttpResponseRedirect('/contact/')
        except:
            # Show an error message if email fails
            messages.error(request,'Failed to send message. Try again!')
    message_list = [message.message for message in messages.get_messages(request)]
    print("Debug: message_list =", message_list)

    return render(request,'contact.html', {'messages': json.dumps(message_list)})

