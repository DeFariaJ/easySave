from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users
import pandas as pd


def index(request):
    myusers = Users.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        "myusers": myusers
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))


def addrecord(request):
    f = request.POST["first"]
    l = request.POST["last"]
    e = request.POST["email"]
    a = request.POST["age"]
    c = request.POST["country"]
    user = Users(firstname=f, lastname=l, email_field=e, age=a, country=c)
    user.save()
    return HttpResponseRedirect(reverse("index"))


def delete(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse("index"))


def update(request, id):
    myuser = Users.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        "myuser": myuser,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    f = request.POST["first"]
    l = request.POST["last"]
    e = request.POST["email"]
    a = request.POST["age"]
    c = request.POST["country"]
    user = Users.objects.get(id=id)
    user.firstname = f
    user.lastname = l
    user.email_field = e
    user.age = a
    user.country = c
    user.save()

    return HttpResponseRedirect(reverse("index"))
