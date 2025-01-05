from django.contrib import admin
from .models import SummerTimetable, WinterTimetable, SeasonalTimetable


# Register your models here.

admin.site.register(SummerTimetable)
admin.site.register(WinterTimetable)
admin.site.register(SeasonalTimetable)