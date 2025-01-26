from modeltranslation.translator import translator, TranslationOptions
from .models import SummerTimetable,WinterTimetable,SeasonalTimetable

class SummerTimetableOptions(TranslationOptions):
    fields = ('days',)

translator.register(SummerTimetable,SummerTimetableOptions)

class WinterTimetableOptions(TranslationOptions):
    fields = ('days',)

translator.register(WinterTimetable,WinterTimetableOptions)

class SeasonalTimetableOptions(TranslationOptions):
    fields = ('dates',)

translator.register(SeasonalTimetable,SeasonalTimetableOptions)