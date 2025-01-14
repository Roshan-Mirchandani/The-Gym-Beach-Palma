from django.db import models

# Create your models here.
class PersonalTrainer(models.Model):
    name = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)
    text = models.CharField(max_length=3000)
    whatsapp_number = models.CharField(max_length=20)
    portrait = models.ImageField(upload_to='static/images/staff/personal_trainers', default='static/images/staff/personal_trainers/default.jpg')

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name =  models.CharField(max_length=100)
    portrait = models.ImageField(upload_to='static/images/staff/personal_trainers', default='static/images/staff/personal_trainers/default.jpg')
    role = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name