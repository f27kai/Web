from django.urls import path
from . import views

urlpatterns = [
    path("name/", views.name_surname_view),
    path("hobby/", views.hobby_view),
    path("datetime/", views.get_datetime_view),
    path("number/", views.random_number_view),
]