from django.conf.urls import url
from django.contrib import admin
from project_manage import views
from django.urls import path

urlpatterns = [
    path('project_manage/',views.project_manage),
    #path('project_add/',views.project_add),


]
