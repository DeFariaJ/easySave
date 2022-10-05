from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.


class Bills(models.Model):
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)


class January(models.Model):
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)


class June(models.Model):
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.fixed_bills


class July(models.Model):
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)


class August(models.Model):
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)


class September(models.Model):
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)


class October(models.Model):
    user = models.ForeignKey(User, related_name="bills",
                             on_delete=models.CASCADE)
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.fixed_bills
