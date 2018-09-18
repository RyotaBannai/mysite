from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('.well-known/acme-challenge/YI7ivk3q0YIK7E1GSpWjaC2kwvDJ4lGeKi8k9AGvHrs', views.acm, name='acm'),
]