from django.urls import path
from .views import *

app_name = 'movie_reviews'

urlpatterns = [
    path('', index, name='index'),
]