from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
   
    path('biteergourd/', views.biteergourd, name='biteergourd'),
    path('bringle/', views.bringle, name='bringle'),
    path('brocoli/', views.brocoli, name='brocoli'),
    path('cabbage/', views.cabbage, name='cabbage'),
    path('chilli/', views.chilli, name='chilli'),
    path('cucumber/', views.cucumber, name='cucumber'),
    path('flower/', views.flower, name='flower'),
    path('marigold/', views.marigold, name='marigold'),
    path('sugarcane/', views.sugarcane, name='sugarcane'),
    path('tomato/', views.tomato, name='tomato'),
    path('watermelon/', views.watermelon, name='watermelon'),
]
