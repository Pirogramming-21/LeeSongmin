from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('post_new/', post_new, name='post_new'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('user/<str:username>/', user_profile, name='user_profile'),
    path('like_post/', like_post, name='like_post'),
]
