from django.urls import path
from cinema.views import cinema_detail, cinema_list


app_name = "cinema"

urlpatterns = [
    path("cinema/", cinema_list, name="cinema_list"),
    path("cinema/<int:pk>/", cinema_detail, name="cinema_detail"),
]
