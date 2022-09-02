from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index_bills"),
    path("add/", views.add, name="add"),
    path("add/addbill/", views.addbill, name="addbill"),
    ######################
    # months index
    #######################
    path("june/", views.june, name="june"),
    path("july/", views.july, name="july"),
    path("august/", views.august, name="august"),
    #######################
    # delete
    #######################
    path("delete/<int:id>", views.deletebill, name="deletebill"),
    path("june/delete/<int:id>", views.delete_jun_bill, name="delete_jun_bill"),
    path("july/delete/<int:id>", views.delete_jul_bill, name="delete_jul_bill"),
    path("august/delete/<int:id>", views.delete_aug_bill, name="delete_aug_bill"),
    #######################
    # update pages
    #######################
    path("update/<int:id>", views.updatebill, name="updatebill"),
    path("june/update/<int:id>", views.update_jun_bill, name="update_jun_bill"),
    path("july/update/<int:id>", views.update_jul_bill, name="update_jul_bill"),
    path("august/update/<int:id>", views.update_aug_bill, name="update_aug_bill"),
    #######################
    # update record
    #######################
    path("update/updaterecordbill/<int:id>",
         views.updatebillrecord, name="updatebillrecord"),
    path("june/update/updaterecordbill/<int:id>",
         views.update_jun_billrecord, name="update_jun_billrecord"),
    path("july/update/updaterecordbill/<int:id>",
         views.update_jul_billrecord, name="update_jul_billrecord"),
    path("august/update/updaterecordbill/<int:id>",
         views.update_aug_billrecord, name="update_aug_billrecord"),

]
