from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from unicodedata import category

from app.models import Car, Category
from app.serializers import CarSerializers, CategorySerializers


class CarApiListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "page_size"
    max_page_size = 2

class CarListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    pagination_class = CarApiListPagination


    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category")
        brand = self.request.query_params.get("brand")
        full_price = self.request.query_params.get("full_price")

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if brand:
            queryset = queryset.filter(brand=brand)
        if full_price:
            queryset = queryset.filter(full_price=full_price)

        return queryset





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
"""
CreateAPIView
ListAPIView

RetrieveAPIView
UpdateAPIView
DestroyAPIView
/<pk>



CRUD - filter, pagination
"""

