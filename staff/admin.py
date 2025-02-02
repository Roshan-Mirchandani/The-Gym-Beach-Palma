from django.contrib import admin
from .models import PersonalTrainer,Staff

# Register your models here.

class PersonalTrainerAdmin(admin.ModelAdmin):
    list_display =('name','languages','whatsapp_number')
    list_editable=('whatsapp_number',) 

admin.site.register(PersonalTrainer,PersonalTrainerAdmin)
   
class StaffAdmin(admin.ModelAdmin):
    list_display =('name','role')

admin.site.register(Staff, StaffAdmin)