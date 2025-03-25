from django.urls import path

from app import views

urlpatterns = [
    path("car/create/", views.CarCreateApi.as_view()),
    path("car/create/list/", views.CarlistApi.as_view()),
    path("car/update/<pk>", views.CarUpdateApiView.as_view()),
    path("car/destroy/<pk>", views.CarDestroyApi.as_view()),
    path("car/list/", views.CarListView.as_view())

]