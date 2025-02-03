from django.shortcuts import render
from .models import GymEquipment, PersonalTrainers, TanningBed
from django.http import Http404

# Create your views here.

def services(request,location ):
    if location not in ['palma', 'inca']:
        raise Http404("Location not found")
     
    ge = GymEquipment.objects.all()
    pt = PersonalTrainers.objects.all()
    tb = TanningBed.objects.all()

    return render(request, f'{location}/services.html',{'gym_equipment': ge, 'personal_trainer' : pt,
                                                         'tanning_bed' : tb, 'location':location } )

