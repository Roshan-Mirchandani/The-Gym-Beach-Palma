from modeltranslation.translator import translator, TranslationOptions
from .models import ExtraPayments, RentCosts

class ExtraPaymentOptions(TranslationOptions):
    fields =('extra_service',)

translator.register(ExtraPayments,ExtraPaymentOptions)

class RentCostsOptions(TranslationOptions):
    fields =('rentable',)

translator.register(RentCosts,RentCostsOptions)