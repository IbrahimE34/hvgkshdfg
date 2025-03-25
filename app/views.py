from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView

from app.models import Car, Category
from app.serializers import CarSerializers, CategorySerializers


class CarCreateApi(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarlistApi(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CarRetrieveApi(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CarUpdateApiView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CarDestroyApi(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
"""
CreateAPIView
ListAPIView

RetrieveAPIView
UpdateAPIView
DestroyAPIView
/<pk>



CRUD - filter, pagination
"""

