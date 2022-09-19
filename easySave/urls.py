
from django.contrib import admin
from django.urls import include, path
from landing.views import landingpage


urlpatterns = [
    path("", landingpage, name="landingpage"),
    path("users/", include("users.urls")),
    path("bills/", include("bills.urls")),
    path('admin/', admin.site.urls),
]
