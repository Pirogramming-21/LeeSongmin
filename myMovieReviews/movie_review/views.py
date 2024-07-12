from django.shortcuts import render, redirect
from .models import Review

def review_list(request):
  reviews = Review.objects.all()
  context = {
    "reviews": reviews,
  }
  return render(request, 'review_list.html', context)

def review_create(request):
  if request.method == "POST":
    Review.objects.create(
      title = request.POST["title"],
      year = request.POST["year"],
      genre = request.POST["genre"],
      score = request.POST["score"],
      running_time = request.POST["running_time"],
      content = request.POST["content"],
      director = request.POST["director"],
      actor= request.POST["actor"]
    )
    return redirect("/reviews")
  return render(request, 'review_create.html')

def review_detail(request, pk):
  review = Review.objects.get(id=pk)
  context = {
    "review": review
  }
  return render(request, 'review_detail.html', context)

def review_update(request, pk):
  review = Review.objects.get(id=pk)
  if request.method=="POST":
    review.title = request.POST["title"]
    review.year = request.POST["year"]
    review.genre = request.POST["genre"]
    review.score = request.POST["score"]
    review.running_time = request.POST["running_time"]
    review.content = request.POST["content"]
    review.director = request.POST["director"]
    review.actor = request.POST["actor"]

    review.save()

    return redirect(f"/reviews/{pk}")
  
  context = {
    "review": review
  }
  return render(request, 'review_update.html', context)

def review_delete(request, pk):
    if request.method=="POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews")