import datetime
from turtle import width
from unicodedata import decimal
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import PayDay
from django.template import loader
from .models import Bills
import pandas as pd
import plotly.express as px

# Create your views here.


def index(request):
    mybills = Bills.objects.all().values()
    template = loader.get_template("index_bills.html")
    ######
    data = pd.DataFrame(mybills)
    total = sum(data["fixed_bills_amount"])
    my_salary = 1240.00
    bills_percent = (float(total)/my_salary)*100
    bills_percent = round(bills_percent)
    #######
    fig = px.pie(data, values=data["fixed_bills_amount"],
                 names=data["fixed_bills"], title="")

    fig.update_layout(
        autosize=False,
        width=600,
        height=600,
    )
    pie_chart = fig.to_html()

    context = {
        "mybills": mybills,
        "total_amount": total,
        "bills_percent": bills_percent,
        "pie_chart": pie_chart,
    }
    #########
    sept_sum = []
    for x in data["pay_date"]:
        x = str(x)
        if x[5:7] == "09":
            print("September")

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
