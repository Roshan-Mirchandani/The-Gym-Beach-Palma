from django.db import models

# Create your models here.

class SummerTimetable(models.Model):
    days = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.days} : {self.time}"

class WinterTimetable(models.Model):
    days = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.days} : {self.time}"

class Season(models.TextChoices):
    SUMMER = 'Summer'
    WINTER = 'Winter'

class SeasonalTimetable(models.Model):
    season = models.CharField(max_length=100, choices=Season.choices, unique=True)
    dates = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.season} : {self.dates}"