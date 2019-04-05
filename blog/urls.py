from django.urls import path
from . import views

urlpatterns = [
    path('', views.Team_List, name='Team_List'),
]
