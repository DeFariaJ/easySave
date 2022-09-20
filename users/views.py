from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import pandas as pd
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        # later we'll log user in here
        return redirect("total")
    else:

        form = UserCreationForm()
        context = {
            "form": form,
        }
    return render(request, "signup.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login uuser
            return redirect("total")

    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)
