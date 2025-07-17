from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.AboutPage, name='about'),
    path('experience/', views.ExperiencePage, name='experience'),
    path('contact/', views.ContactPage, name='contact'),
]