from django.shortcuts import render,redirect
from django.utils.translation import activate, get_language
from django.conf import settings
from django.http import Http404



def home_view(request, location):
    if location not in ['palma', 'inca']:
        raise Http404("Location not found")
    return render(request,f'{location}/index.html',  {
        'LANGUAGE_CODE': request.LANGUAGE_CODE,
        'location' : location 
    })








