from turtle import home
from django.urls import path
from .views import about_list
app_name = 'aboutus'
urlpatterns = [
    path('', about_list, name='aboutus_list')
]