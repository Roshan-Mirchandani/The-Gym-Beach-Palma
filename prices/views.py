from django.shortcuts import render
from .models import OneTimePayments, InitialPayment,MonthlyPayments, ExtraPayments, RentCosts

# Create your views here.
def prices(request):
    one_time_payments = OneTimePayments.objects.all()
    initial_payment = InitialPayment.objects.get()
    monthly_payments = MonthlyPayments.objects.all()
    extra_payments = ExtraPayments.objects.all()
    rent_costs = RentCosts.objects.all()

    data = {'one_time_payments' : one_time_payments, 'initial_payment' : initial_payment,
             'monthly_payments' : monthly_payments, 'extra_payments' : extra_payments,
              'rent_costs' : rent_costs}
    return render(request, 'prices/prices.html', data)