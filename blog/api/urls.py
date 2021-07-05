from django.urls import path
from blog.api import views

app_name = 'blog'

urlpatterns = [
    path('<int:id>', views.post_detail_api, name='post'),
    path('<int:id>/update', views.update_post_api, name='update'),
    path('<int:id>/delete', views.delete_post_api, name='delete'),
    path('create/', views.create_post_api, name='create')

]

