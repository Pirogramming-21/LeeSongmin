from django.urls import path
from .views import *

app_name = 'movie_review'

urlpatterns = [
    path('', review_list),
    path('/create', review_create),
    path('/<int:pk>', review_detail),
    path('/<int:pk>/update', review_update),
    path('/<int:pk>/delete', review_delete),
]