from django import forms
from .models import Users
from django.forms import ModelForm


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["firstname", "lastname", "age", "country", "email_field"]
