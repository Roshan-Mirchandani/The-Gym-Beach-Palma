from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages  # To show success/error messages
from django.http import HttpResponseRedirect 
from django.utils.translation import gettext as _
import json

# Create your views here.

def contact(request, location=None):
    if request.method == 'POST':
        print("if working")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('query')
        number = request.POST.get('number')

        subject = f"New Query from {name}"
        full_message = f" Name: {name}\n Email: {email} \n Phone Number: {number}\n \n  {message} \n"
        print("message successfuly received") # used strictly for debuggin purposes
        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_RECEIVER],
                fail_silently=False
            )
            succes_message = _('Your query has been sent successfully!')
            messages.success(request,succes_message )
            print("message successfuly sent") # used strictly for debuggin purposes
            return HttpResponseRedirect('/contact/')
        except:
            # Show an error message if email fails
            fail_message =_('Failed to send message. Try again!')
            messages.error(request,fail_message)
            print("message not sent") # used strictly for debuggin purposes
    message_list = [message.message for message in messages.get_messages(request)]
    

    return render(request,'contact.html', {'messages': json.dumps(message_list), 'location':location})

