from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('<int:id>/', views.post, name='post')
    ]