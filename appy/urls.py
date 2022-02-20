from django import urls
from django.contrib import admin
from django.urls import path
from . import views

import appy

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('',views.home,name="home"),
    path('Searched_Coin',views.searched,name="Search-Box"),
    path('About',views.about,name="About"),
]

