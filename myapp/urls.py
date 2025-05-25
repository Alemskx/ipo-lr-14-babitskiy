

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_project/', views.about_project, name='about_project'),
]
