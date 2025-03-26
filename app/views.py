from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from unicodedata import category

from app.filters import CarFilter
from app.models import Car
from app.serializers import CarSerializers, CategorySerializers


class CarApiListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page_size"
    max_page_size = 2

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    pagination_class = CarApiListPagination




class CarCreateApi(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarlistApi(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    pagination_class = CarApiListPagination


class CarRetrieveApi(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CarUpdateApiView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CarDestroyApi(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

    filter_backends = [DjangoFilterBackend]
    filter_class = CarFilter
    def filter_queryset(self, queryset):


        filterset = self.filter_class(self.request.GET, queryset=queryset)

        if not filterset.is_valid():
            raise ValidationError(filterset.errors)

        filtered_qs = filterset.qs

        if not filtered_qs.exists():
            raise NotFound({
                "detail": "По вашему запросу ничего не найдено. Попробуйте изменить критерии фильтрации."
            })

        return filtered_qs




"""
CreateAPIView
ListAPIView

RetrieveAPIView
UpdateAPIView
DestroyAPIView
/<pk>



CRUD - filter, pagination
"""

