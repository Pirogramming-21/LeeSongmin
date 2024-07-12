from django.urls import path
from .views import *

app_name = 'movie_review'

urlpatterns = [
    path('', movie_list),
    path('/create', movie_create),
]