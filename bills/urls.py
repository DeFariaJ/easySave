from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_bills"),
    path("add/", views.add, name="add"),
    path("add/addbill/", views.addbill, name="addbill"),
    path("delete/<int:id>", views.deletebill, name="deletebill"),
    path("update/<int:id>", views.updatebill, name="updatebill"),
    path("update/updaterecordbill/<int:id>",
         views.updatebillrecord, name="updatebillrecord"),



]
