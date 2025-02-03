from django.shortcuts import render
from .models import SummerTimetable,WinterTimetable,SeasonalTimetable
from django.http import Http404

# Create your views here.
def timetable(request, location):
    if location not in ['palma', 'inca']:
        raise Http404("Location not found")
    
    stt = SummerTimetable.objects.all()
    wt = WinterTimetable.objects.all()
    ss = SeasonalTimetable.objects.filter(season="Summer").first()
    ws = SeasonalTimetable.objects.filter(season="Winter").first()
    data = {
        'summer_timetable' : stt, 'winter_timetable' : wt, 'summer_season':ss , "winter_season" : ws,'location':location }
    
    return render(request,f'{location}/timetable.html',data)