from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_bills"),
    path("add", views.add, name="add"),
    path("add/addbill", views.addbill, name="addbills"),


]
