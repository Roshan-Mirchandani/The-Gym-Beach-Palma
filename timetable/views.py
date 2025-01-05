from django.shortcuts import render
from .models import SummerTimetable,WinterTimetable,SeasonalTimetable

# Create your views here.
def timetable(request):
    stt = SummerTimetable.objects.all()
    wt = WinterTimetable.objects.all()
    ss = SeasonalTimetable.objects.filter(season="Summer").first()
    ws = SeasonalTimetable.objects.filter(season="Winter").first()
    data = {
        'summer_timetable' : stt, 'winter_timetable' : wt, 'summer_season':ss , "winter_season" : ws  }
    
    return render(request,'timetable.html',data)