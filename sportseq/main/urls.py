from django.urls import path
from . import views


urlpatterns = [path("", views.home, name="home"),
               path("lend/", views.lendItem, name="lend"),
               path("status/", views.status, name="status"),
               path("return/", views.returnItem, name="return"),

               ]
