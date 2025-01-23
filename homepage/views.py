from django.shortcuts import render,redirect
from django.utils.translation import activate, get_language
from django.conf import settings

def home_view(request):
    return render(request,'homepage/index.html',  {
        'LANGUAGE_CODE': request.LANGUAGE_CODE
    })








