from django.http import HttpResponse
from django.shortcuts import render


def landingpage(request):
    return render(request, "landing_page.html")
