from django.urls import path
from . import views

urlpatterns = [
    path('', views.forbidden, name='forbidden'),
]
