from django.urls import path
from . import views

app_name='info'
urlpatterns = [
    path('', views.home, name='about'),
    path('contact/', views.contact, name='contacts'),
]
