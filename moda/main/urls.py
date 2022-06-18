from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('top', views.top, name='top'),
]
