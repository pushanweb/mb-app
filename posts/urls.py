# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:25:48 2020

@author: Pushan
"""


from django.urls import path
from .views import HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]