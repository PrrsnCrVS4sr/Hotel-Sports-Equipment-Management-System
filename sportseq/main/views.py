
from asyncio.windows_events import NULL
from django.shortcuts import render
import requests
import json
# Create your views here.


def home(response):
    return render(response, "main/home.html")


def lendItem(response):
    item = {}
    if response.method == "POST":
        if response.POST.get("lend"):
            item['name'] = response.POST.get("lend")
            if(response.POST.get(item['name']).isdigit()):
                item['user'] = int(response.POST.get(item['name']))
            requests.put("http://127.0.0.1:8000/items/lend",
                         json=item)
    requestItems = requests.get("http://127.0.0.1:8000/items/status")
    ls = requestItems.json()
    return render(response, "main/lend.html", {"ls": ls})


def returnItem(response):
    item = {}
    if response.method == "POST":
        item['name'] = response.POST.get("return")
        requests.put("http://127.0.0.1:8000/items/return",
                     json=item)
    requestItems = requests.get("http://127.0.0.1:8000/items/status")
    requestUsers = requests.get("http://127.0.0.1:8000/users/")
    ls = requestItems.json()
    users = requestUsers.json()
    return render(response, "main/return.html", {"ls": ls, "users": users})


def status(response):
    requestItems = requests.get("http://127.0.0.1:8000/items/status")
    requestUsers = requests.get("http://127.0.0.1:8000/users/")
    ls = requestItems.json()
    users = requestUsers.json()
    return render(response, "main/status.html", {"ls": ls, "users": users})
