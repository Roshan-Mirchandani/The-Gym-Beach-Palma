from django.shortcuts import render
from .models import GymEquipment, PersonalTrainers, TanningBed

# Create your views here.

def services(request):
    ge = GymEquipment.objects.all()
    pt = PersonalTrainers.objects.all()
    tb = TanningBed.objects.all()
    return render(request, 'services.html',{'gym_equipment': ge, 'personal_trainer' : pt, 'tanning_bed' : tb} )

