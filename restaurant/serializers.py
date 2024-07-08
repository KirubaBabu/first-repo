from rest_framework import serializers
from .models import MenuTable, BookingTable
from django.contrib.auth.models import User
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'