import datetime
from re import template
from turtle import color
from unicodedata import decimal
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import PayDay
from django.template import loader
from .models import August, Bills, January, July, June, September
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

    return HttpResponse(template.render(context, request))


###### JUNE ########


def june(request):
    mybills = June.objects.all().values()
    template = loader.get_template("june.html")
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

    return HttpResponse(template.render(context, request))

###### JUlY ########


def july(request):
    mybills = July.objects.all().values()
    template = loader.get_template("july.html")
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

    return HttpResponse(template.render(context, request))

###### AUGUST ########


def august(request):
    mybills = August.objects.all().values()
    template = loader.get_template("august.html")
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

    return HttpResponse(template.render(context, request))


###### SEPTEMBER ########
def september(request):
    mybills = September.objects.all().values()
    template = loader.get_template("september.html")
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

    return HttpResponse(template.render(context, request))

#############################################################################
# ADD
#############################################################################


def add(request):
    form = PayDay()
    context = {
        "form": form
    }
    return render(request, "add_bills.html", context)


def addbill(request):
    x = request.POST["fixed_bills"]
    y = request.POST["fixed_bills_amount"]
    z = request.POST["pay_date"]
    if z[5:7] == "01":
        bill = January(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
        bill.save()
        return HttpResponseRedirect(reverse("january"))
    elif z[5:7] == "06":
        bill = June(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
        bill.save()
        return HttpResponseRedirect(reverse("june"))
    elif z[5:7] == "07":
        bill = July(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
        bill.save()
        return HttpResponseRedirect(reverse("july"))
    elif z[5:7] == "08":
        bill = August(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
        bill.save()
        return HttpResponseRedirect(reverse("august"))
    elif z[5:7] == "09":
        bill = September(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
        bill.save()
        return HttpResponseRedirect(reverse("september"))
    else:
        bill = Bills(fixed_bills=x, fixed_bills_amount=y, pay_date=z)
        bill.save()
    return HttpResponseRedirect(reverse("index_bills"))


#############################################################################
# DELETE
#############################################################################

def deletebill(request, id):
    bill = Bills.objects.get(id=id)
    bill.delete()
    return HttpResponseRedirect(reverse("index_bills"))


def delete_jan_bill(request, id):
    bill = January.objects.get(id=id)
    bill.delete()
    return HttpResponseRedirect(reverse("january"))


def delete_jun_bill(request, id):
    bill = June.objects.get(id=id)
    bill.delete()
    return HttpResponseRedirect(reverse("june"))


def delete_jul_bill(request, id):
    bill = July.objects.get(id=id)
    bill.delete()
    return HttpResponseRedirect(reverse("july"))


def delete_aug_bill(request, id):
    bill = August.objects.get(id=id)
    bill.delete()
    return HttpResponseRedirect(reverse("august"))


def delete_sep_bill(request, id):
    bill = September.objects.get(id=id)
    bill.delete()
    return HttpResponseRedirect(reverse("september"))


#############################################################################
# UPDATE (page)
#############################################################################


def updatebill(request, id):
    mybill = Bills.objects.get(id=id)
    form = PayDay(instance=mybill)
    context = {
        "mybill": mybill,
        "form": form,
    }
    return render(request, "update_bills.html", context)


def update_jan_bill(request, id):
    mybill = January.objects.get(id=id)
    form = PayDay(instance=mybill)
    context = {
        "mybill": mybill,
        "form": form,
    }
    return render(request, "update_bills.html", context)


def update_jun_bill(request, id):
    mybill = June.objects.get(id=id)
    form = PayDay(instance=mybill)
    context = {
        "mybill": mybill,
        "form": form,
    }
    return render(request, "update_bills.html", context)


def update_jul_bill(request, id):
    mybill = July.objects.get(id=id)
    form = PayDay(instance=mybill)
    context = {
        "mybill": mybill,
        "form": form,
    }
    return render(request, "update_bills.html", context)


def update_aug_bill(request, id):
    mybill = August.objects.get(id=id)
    form = PayDay(instance=mybill)
    context = {
        "mybill": mybill,
        "form": form,
    }
    return render(request, "update_bills.html", context)


def update_sep_bill(request, id):
    mybill = September.objects.get(id=id)
    form = PayDay(instance=mybill)
    context = {
        "mybill": mybill,
        "form": form,
    }
    return render(request, "update_bills.html", context)

#############################################################################
# UPDATE (record)
#############################################################################


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


def update_jan_billrecord(request, id):
    billrecord = request.POST["fixed_bills"]
    bill_amount = request.POST["fixed_bills_amount"]
    pay_date = request.POST["pay_date"]

    bill = January.objects.get(id=id)
    bill.fixed_bills = billrecord
    bill.fixed_bills_amount = bill_amount
    bill.pay_date = pay_date
    bill.save()
    return HttpResponseRedirect(reverse("january"))


def update_jun_billrecord(request, id):
    billrecord = request.POST["fixed_bills"]
    bill_amount = request.POST["fixed_bills_amount"]
    pay_date = request.POST["pay_date"]

    bill = June.objects.get(id=id)
    bill.fixed_bills = billrecord
    bill.fixed_bills_amount = bill_amount
    bill.pay_date = pay_date
    bill.save()
    return HttpResponseRedirect(reverse("june"))


def update_jul_billrecord(request, id):
    billrecord = request.POST["fixed_bills"]
    bill_amount = request.POST["fixed_bills_amount"]
    pay_date = request.POST["pay_date"]

    bill = July.objects.get(id=id)
    bill.fixed_bills = billrecord
    bill.fixed_bills_amount = bill_amount
    bill.pay_date = pay_date
    bill.save()
    return HttpResponseRedirect(reverse("july"))


def update_aug_billrecord(request, id):
    billrecord = request.POST["fixed_bills"]
    bill_amount = request.POST["fixed_bills_amount"]
    pay_date = request.POST["pay_date"]

    bill = August.objects.get(id=id)
    bill.fixed_bills = billrecord
    bill.fixed_bills_amount = bill_amount
    bill.pay_date = pay_date
    bill.save()
    return HttpResponseRedirect(reverse("august"))


def update_sep_billrecord(request, id):
    billrecord = request.POST["fixed_bills"]
    bill_amount = request.POST["fixed_bills_amount"]
    pay_date = request.POST["pay_date"]

    bill = September.objects.get(id=id)
    bill.fixed_bills = billrecord
    bill.fixed_bills_amount = bill_amount
    bill.pay_date = pay_date
    bill.save()
    return HttpResponseRedirect(reverse("september"))


#############################################################################
# TOTAL BILLS EXPENSES
#############################################################################

def total(request):
    june = June.objects.all().values()
    july = July.objects.all().values()
    august = August.objects.all().values()

    df_june = pd.DataFrame(june)
    df_july = pd.DataFrame(july)
    df_august = pd.DataFrame(august)

    # Internet
    month_ll_NOS = [["June", int(df_june.loc[df_june.fixed_bills == "NOS", "fixed_bills_amount"])],
                    ["July", int(df_july.loc[df_june.fixed_bills ==
                                             "NOS", "fixed_bills_amount"])],
                    ["August", int(df_august.loc[df_june.fixed_bills == "NOS", "fixed_bills_amount"])]]

    df_total = pd.DataFrame(month_ll_NOS, columns=["Month", "Amount(€)"])
    fig = px.bar(df_total, x="Month", y="Amount(€)", color="Month")

    fig.update_layout(
        title_font_color="black",
        showlegend=False,
        autosize=False,
        width=600,
        height=400,
        xaxis_title="",
        title={
            "text": "<b>Internet + Phone</b>",
            "y": 0.99,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",

        }
    )
    bar_chart = fig.to_html()

    # water
    month_ll_water = [["June", int(df_june.loc[df_june.fixed_bills == "Water", "fixed_bills_amount"])],
                      ["July", int(df_july.loc[df_june.fixed_bills ==
                                   "Water", "fixed_bills_amount"])],
                      ["August", int(df_august.loc[df_june.fixed_bills == "Water", "fixed_bills_amount"])]]

    df_total_Water = pd.DataFrame(
        month_ll_water, columns=["Month", "Amount(€)"])
    fig2 = px.line(df_total_Water, x="Month", y="Amount(€)",
                   range_y=[0, 60], markers=True)
    fig2.update_layout(
        title_font_color="black",
        showlegend=False,
        autosize=False,
        width=600,
        height=400,
        xaxis_title="",
        title={
            "text": "<b>Water</b>",
            "y": 0.99,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",

        }
    )
    line_chart = fig2.to_html()

    template = loader.get_template("total.html")
    context = {
        "june": june,
        "july": july,
        "bar_chart": bar_chart,
        "line_chart": line_chart,
    }
    return HttpResponse(template.render(context, request))
