from django.contrib import admin
from .models import SummerTimetable, WinterTimetable, SeasonalTimetable


# Register your models here.
class SummerTimetableAdmin(admin.ModelAdmin):
    list_display =('days','time')
    list_editable =('time',)
    ordering = ('days',)

admin.site.register(SummerTimetable, SummerTimetableAdmin)

class WinterTimetableAdmin(admin.ModelAdmin):
    list_display =('days','time')
    list_editable =('time',)
    ordering = ('days',)

admin.site.register(WinterTimetable, WinterTimetableAdmin)

class SeasonalTimetableAdmin(admin.ModelAdmin):
    list_display =('season','dates')
    ordering = ('season',)

admin.site.register(SeasonalTimetable, SeasonalTimetableAdmin)