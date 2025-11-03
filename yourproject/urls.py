from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def router_home(request):
    return render(request, "router.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", router_home, name="router"),
    path("", include("mturkrouter.urls")),
]
