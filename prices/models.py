from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class OneTimePayments(models.Model):
    days = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"{self.days} days - €{self.price}"


class InitialPayment(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"€{self.price}"


class PaymentMethod(models.TextChoices):
    CASH = 'Cash', _('Cash')
    CARD = 'Card', _('Card')
    

class MonthlyPayment(models.Model):
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices, unique=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"{self.payment_method} - €{self.price}"


class ExtraPayment(models.Model):
    extra_service = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    def __str__(self):
        return f"{self.extra_service} - €{self.price}"


class RentCost(models.Model):
    rentable =  models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return f"Rent a {self.rentable} - €{self.price}"
    
