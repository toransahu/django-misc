from django.urls import path
from . import views

urlpatterns = [
    # path('', views.foo, name='Hello'),            
    path('bar/', views.bar, name='Bar')            
]

