from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign, name='sign'),
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('old_diary_entries/', views.old, name='old'),
    path('old_diary_entries/view/', views.view, name='view')
]