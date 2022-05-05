import imp
from os import stat
from django.http import JsonResponse
from main.models import SportItem, User
from .serializers import SportItemSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from sportseq import serializers
import json

null = None

# Requests for Sport Items


def verifyData(data, items, users, op):
    if op == "lend":
        if 'user' in data.keys():
            for user in users:
                if data['user'] == user.rollNo:
                    for item in items:
                        if data['name'] == item.name:
                            return item.id
        else:
            return 0
    if op == "return":
        if 'name' in data.keys():
            for item in items:
                if data['name'] == item.name:
                    return item.id
        else:
            return 0


@api_view(['GET'])
def sport_item_status(request):
    items = SportItem.objects.all()
    # For recieving the status of all items
    if request.method == "GET":

        serializer = SportItemSerializer(items, many=True)
        return Response(serializer.data)
    # For adding an item(not done via frontend)


@api_view(['POST'])
def sport_item_add(request):
    if request.method == 'POST':
        #data = verifyData(request.data)
        serializer = SportItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def sport_item_lend(request):
    users = User.objects.all()
    items = SportItem.objects.all()
    if request.method == 'PUT':

        data = request.data
        itemID = verifyData(data, items, users, "lend")
        item = SportItem.objects.get(pk=itemID)
        if itemID:
            data['isBorrowed'] = True
            serializer = SportItemSerializer(item, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def sport_item_return(request):
    users = User.objects.all()
    items = SportItem.objects.all()
    if request.method == 'PUT':
        data = request.data

        itemID = verifyData(data, items, users, "return")
        item = SportItem.objects.get(pk=itemID)
        if itemID:
            data['isBorrowed'] = False
            data['user'] = null
            serializer = SportItemSerializer(item, data=data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def sport_item_delete(request, id):
    try:
        item = SportItem.objects.get(pk=id)
    except SportItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Requests for Users
@api_view(['GET', 'POST'])
def userGetPost(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def userGetPutDelete(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
