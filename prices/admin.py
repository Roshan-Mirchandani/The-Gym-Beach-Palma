from django.contrib import admin
from .models import OneTimePayments, InitialPayment,MonthlyPayments, ExtraPayments, RentCosts

# Register your models here.

admin.site.register(OneTimePayments)
admin.site.register(InitialPayment)
admin.site.register(MonthlyPayments)
admin.site.register(ExtraPayments)
admin.site.register(RentCosts)



