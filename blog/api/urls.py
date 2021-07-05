from django.urls import path
from blog.api.views import post_detail_api

app_name = 'blog'

urlpatterns = [
    path('<int:id>', post_detail_api, name='post')
]

