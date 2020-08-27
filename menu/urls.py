from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('flush_session/', views.flush_session, name='flush_session'),

]