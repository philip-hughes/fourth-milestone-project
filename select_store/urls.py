from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_store, name='select_store')
]