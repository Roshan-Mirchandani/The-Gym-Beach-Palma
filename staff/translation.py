from modeltranslation.translator import translator, TranslationOptions
from .models import PersonalTrainer,Staff

class PersonalTrainerOptions(TranslationOptions):
    fields = ('languages', 'text',)

translator.register(PersonalTrainer,PersonalTrainerOptions)

class StaffOptions(TranslationOptions):
    fields = ('role',)

translator.register(Staff,StaffOptions)