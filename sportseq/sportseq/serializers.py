from rest_framework import serializers
from main.models import SportItem, User


class SportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportItem
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
