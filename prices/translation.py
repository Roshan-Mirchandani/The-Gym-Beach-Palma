from modeltranslation.translator import translator, TranslationOptions
from .models import ExtraPayment, RentCost

class ExtraPaymentOptions(TranslationOptions):
    fields =('extra_service',)

translator.register(ExtraPayment,ExtraPaymentOptions)

class RentCostOptions(TranslationOptions):
    fields =('rentable',)

translator.register(RentCost,RentCostOptions)