
from asyncio.windows_events import NULL
from django.shortcuts import render
import requests
import json
# Create your views here.


def home(response):
    return render(response, "main/home.html")


def lendItem(response):

    requestItems = requests.get("http://127.0.0.1:8000/items/")
    requestUsers = requests.get("http://127.0.0.1:8000/users/")
    ls = requestItems.json()
    users = requestUsers.json()
    if response.method == "POST":
        if response.POST.get("lend"):
            for item in ls:
                for user in users:
                    if response.POST.get("c"+str(item['id'])) == str(user['rollNo']):

                        item['isBorrowed'] = True
                        item['user'] = user['id']
                        requests.put("http://127.0.0.1:8000/items/"+str(item['id']),
                                     json=item)
    return render(response, "main/lend.html", {"ls": ls})


def returnItem(response):
    requestItems = requests.get("http://127.0.0.1:8000/items/")
    requestUsers = requests.get("http://127.0.0.1:8000/users/")
    users = requestUsers.json()
    ls = requestItems.json()

    if response.method == "POST":
        for item in ls:
            if response.POST.get("c"+str(item['id'])) == "return":
                item['isBorrowed'] = False
                requests.put("http://127.0.0.1:8000/items/"+str(item['id']),
                             json=item)

    return render(response, "main/return.html", {"ls": ls, "users": users})


def status(response):
    requestItems = requests.get("http://127.0.0.1:8000/items/")
    requestUsers = requests.get("http://127.0.0.1:8000/users/")
    ls = requestItems.json()
    users = requestUsers.json()
    return render(response, "main/status.html", {"ls": ls, "users": users})
