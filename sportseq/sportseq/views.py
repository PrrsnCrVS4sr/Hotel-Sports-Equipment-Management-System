import imp
from os import stat
from django.http import JsonResponse
from main.models import SportItem, User
from .serializers import SportItemSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from sportseq import serializers

null = None

# Requests for Sport Items


def verifyData(data):
    if data['isBorrowed'] == False or data['user'] == null:
        data['user'] = null
        data['isBorrowed'] = False
    return data


@api_view(['GET', 'POST'])
def sportItemGetPost(request):
    # For recieving the status of all items
    if request.method == "GET":
        items = SportItem.objects.all()
        serializer = SportItemSerializer(items, many=True)
        return Response(serializer.data)
    # For adding an item(not done via frontend)
    if request.method == 'POST':
        data = verifyData(request.data)
        serializer = SportItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sportItemGetPutDelete(request, id):
    try:
        item = SportItem.objects.get(pk=id)
    except SportItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SportItemSerializer(item)
        return Response(serializer.data)
    elif request.method == "PUT":
        data = verifyData(request.data)
        serializer = SportItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
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
