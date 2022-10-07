from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="_indexPage_"),
    path("members", views.members, name="_listOfMembers_"),
    path("refreshPage", views.refreshChat, name="_refreshChat_"),

    path('<str:any>', views.warning, name="_badURL_"),
    # Идет послденим, т.к. сначала проверяем которые есть, а если нету, то это он
]
