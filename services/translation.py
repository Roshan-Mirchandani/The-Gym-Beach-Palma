from modeltranslation.translator import translator, TranslationOptions
from .models import GymEquipment, PersonalTrainers, TanningBed

class GymEquipmentOptions(TranslationOptions):
    fields =('name','description',)

translator.register(GymEquipment,GymEquipmentOptions)

class PersonalTrainersOptions(TranslationOptions):
    fields =('type','description',)

translator.register(PersonalTrainers,PersonalTrainersOptions)

class TanningBedOptions(TranslationOptions):
    fields = ('name','description',)
    
translator.register(TanningBed,TanningBedOptions)