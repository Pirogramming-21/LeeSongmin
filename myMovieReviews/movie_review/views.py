from django.shortcuts import render, redirect
from .models import Review

def movie_list(request):
  reviews = Review.objects.all()
  context = {
    "reviews": reviews
  }
  return render(request, 'review_list.html', context)

def movie_create(request):
  if request.method == "POST":
    Review.objects.create(
      title = request.POST["title"],
      year = request.POST["year"],
      genre = request.POST["genre"],
      score = request.POST["score"],
      running_time = request.POST["running_time"],
      content = request.POST["content"],
      director = request.POST["director"],
      actors= request.POST["actors"]
    )
    return redirect("/reviews")
  return render(request, 'review_create.html')