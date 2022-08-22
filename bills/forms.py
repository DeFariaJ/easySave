
from django import forms


class PayDay(forms.Form):
    fixed_bills = forms.CharField(label="Add bill", max_length=200)
    fixed_bills_amount = forms.DecimalField(
        label="Add amount", max_digits=10, decimal_places=2)
    pay_date = forms.DateField(label="Add payment date")
