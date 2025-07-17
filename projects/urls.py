from django.urls import path
from projects import views


urlpatterns = [
    path('projects/', views.projects_lists_view, name='projects_lists'),
]