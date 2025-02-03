from django.shortcuts import render
from .models import PersonalTrainer, Staff
from django.http import Http404

# Create your views here.
def staff(request, location):
    if location not in ['palma', 'inca']:
        raise Http404("Location not found")
    
    pt = PersonalTrainer.objects.all()
    st = Staff.objects.all()

    return render(request,f'{location}/staff.html',{"personal_trainer" : pt, "staff" : st, "location":location})