from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('personalized_learning/', views.personalized_learning, name="personalized_learning"),
    path('resources/', views.resources, name="resources"),
    path('contact/', views.contact, name="contact"),
    path('survey1/', views.survey1, name="survey1"),
    path('survey2/', views.survey2, name="survey2"),
]


