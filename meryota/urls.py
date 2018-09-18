from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('.well-known/acme-challenge/acme-challenge/<slug:slug>', views.acm, name='acm'),
]