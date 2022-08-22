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

    #fixed_bills = forms.CharField(label="Add bill", max_length=200)
    # fixed_bills_amount = forms.DecimalField(
     #   label="Add amount", max_digits=10, decimal_places=2)
    #pay_date = forms.DateField(label="Add payment date")
