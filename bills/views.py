import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import PayDay
from django.template import loader
from .models import Bills

# Create your views here.


def index(request):
    mybills = Bills.objects.all().values()
    template = loader.get_template("index_bills.html")
    context = {
        "mybills": mybills,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    form = PayDay()
    context = {
        "form": form
    }
    return render(request, "test_forms.html", context)


def addbill(request):
    x = request.POST["bill"]
    y = request.POST["amount"]
    z = request.POST["date"]
    bill = Bills(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
    bill.save()
    return HttpResponseRedirect(reverse, ("index_bills.html"))
