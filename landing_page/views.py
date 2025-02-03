from django.shortcuts import render
from django.http import Http404

# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

def gym_location(request, location):
    if location not in ['palma', 'inca']:
        raise Http404("Location not found")
    return render(request, f'{location}/index.html', {'location' : location })