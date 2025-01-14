from django.shortcuts import render
from .models import PersonalTrainer, Staff

# Create your views here.
def staff(request):
    pt = PersonalTrainer.objects.all()
    st = Staff.objects.all()
    return render(request,'staff.html',{"personal_trainer" : pt, "staff" : st})