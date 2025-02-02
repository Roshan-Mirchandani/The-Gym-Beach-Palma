from django.contrib import admin
from .models import OneTimePayments, InitialPayment,MonthlyPayment, ExtraPayment, RentCost

# Register your models here.
admin.site.register(InitialPayment)

class OneTimePaymentsAdmin(admin.ModelAdmin):
    list_display= ('days','price') 
    list_editable = ('price',) 
    ordering =('days',)

admin.site.register(OneTimePayments, OneTimePaymentsAdmin)

class MontlyPaymentAdmin(admin.ModelAdmin):
    list_display= ('payment_method','price')
    list_editable = ('price',)
    ordering =('price',) 

admin.site.register(MonthlyPayment, MontlyPaymentAdmin)

class ExtraPaymentAdmin(admin.ModelAdmin):
    list_display = ('extra_service', 'price')
    list_editable = ('price',) 

admin.site.register(ExtraPayment, ExtraPaymentAdmin)

class RentCostAdmin(admin.ModelAdmin):
    list_display = ('rentable', 'price')
    list_editable = ('price',) 

admin.site.register(RentCost, RentCostAdmin)



