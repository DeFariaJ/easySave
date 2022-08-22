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
    x = request.POST["fixed_bills"]
    y = request.POST["fixed_bills_amount"]
    z = request.POST["pay_date"]
    bill = Bills(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
    bill.save()
    return HttpResponseRedirect(reverse("index_bills"))


def deletebill(request, id):
    bill = Bills.objects.get(id=id)
    bill.delete()
    return HttpResponseRedirect(reverse("index_bills"))


def updatebill(request, id):
    mybill = Bills.objects.get(id=id)
    form = PayDay(instance=mybill)
    context = {
        "mybill": mybill,
        "form": form,
    }
    return render(request, "update_bills.html", context)


def updatebillrecord(request, id):
    billrecord = request.POST["fixed_bills"]
    bill_amount = request.POST["fixed_bills_amount"]
    pay_date = request.POST["pay_date"]

    bill = Bills.objects.get(id=id)
    bill.fixed_bills = billrecord
    bill.fixed_bills_amount = bill_amount
    bill.pay_date = pay_date
    bill.save()
    return HttpResponseRedirect(reverse("index_bills"))
