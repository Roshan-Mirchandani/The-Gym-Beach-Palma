from django.shortcuts import render
from .models import OneTimePayments, InitialPayment,MonthlyPayment, ExtraPayment, RentCost
from django.http import Http404

# Create your views here.
def prices(request,location):
    one_time_payments = OneTimePayments.objects.all()
    initial_payment = InitialPayment.objects.get()
    monthly_payments = MonthlyPayment.objects.all()
    extra_payments = ExtraPayment.objects.all()
    rent_costs = RentCost.objects.all()

    data = {'one_time_payments' : one_time_payments, 'initial_payment' : initial_payment,
             'monthly_payments' : monthly_payments, 'extra_payments' : extra_payments,
              'rent_costs' : rent_costs, 'location': location}
    
    if location not in ['palma', 'inca']:
        raise Http404("Location not found")
    return render(request, f'{location}/prices.html', data)