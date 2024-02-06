# main_app/urls.py
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.main, name='main'),
]
