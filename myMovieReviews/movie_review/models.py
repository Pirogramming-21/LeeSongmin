from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=40)
    year = models.CharField(max_length=10)
    genre = models.CharField(max_length=10)
    score = models.CharField(max_length=10)
    running_time = models.CharField(max_length=20)
    content = models.TextField()
    director = models.CharField(max_length=20)
    actors = models.CharField(max_length=20)