"""sportseq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('items/lend', views.sport_item_lend),
    path('items/return', views.sport_item_return),
    path('items/status', views.sport_item_status),
    path('items/add', views.sport_item_add),
    path('items/<int:id>', views.sport_item_delete),
    path('users/', views.userGetPost),
    path('users/<int:id>', views.userGetPutDelete)

]
