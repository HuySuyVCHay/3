from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('calc/<int:a>/<int:b>/', views.calc, name='calc'),
]