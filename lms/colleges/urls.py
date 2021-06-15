from django.contrib import admin
from django.urls import path
from . import views

app_name = 'colleges'

urlpatterns = [
    path(' ', views.StandardListView.as_view(), name='standard_list'),

]
