from django.urls import path
from . import views

app_name = "listas"
urlpatterns = [
    path("", views.index, name="index"),
    path("crear/", views.add, name="add"),
]