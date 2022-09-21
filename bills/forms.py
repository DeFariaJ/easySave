from django import forms
from django.forms import ModelForm
from bills.models import Bills


class DateInput(forms.DateInput):
    input_type = "date"


class PayDay(forms.ModelForm):
    class Meta:
        widgets = {"pay_date": DateInput()}
        model = Bills
        fields = ["fixed_bills", "fixed_bills_amount", "pay_date"]
