from django.db import models
from datetime import datetime, date
# Create your models here.


class Bills(models.Model):
    fixed_bills = models.CharField(max_length=255)
    fixed_bills_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
