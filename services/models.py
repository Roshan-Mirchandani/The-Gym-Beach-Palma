from django.db import models

# Create your models here.

class GymEquipment(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/services/gym_equipment')
    description = models.TextField()

    def __str__(self):
        return self.name
    
class PersonalTrainers(models.Model):
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/services/personal_trainer')
    description = models.TextField()

    def __str__(self):
        return self.type

class TanningBed(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/services/tanning_bed')
    description = models.TextField()