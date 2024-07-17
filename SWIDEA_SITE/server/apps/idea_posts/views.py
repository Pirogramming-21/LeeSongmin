from django.shortcuts import render,redirect, get_object_or_404
from .models import IdeaPost
from .forms import IdeaPostForm

def main(req):
  ideaposts = IdeaPost.objects.all()
  ctx = {'ideaposts' : ideaposts}
  return render(req, 'ideaposts/list.html',ctx)

def create(req):
  if req.method == "GET":
    ideaform = IdeaPostForm()
    ctx = {'ideaform':ideaform}
    return render(req, 'ideaposts/create.html',ctx)
  ideaform = IdeaPostForm(req.POST, req.FILES)
  if ideaform.is_valid():
    ideaform.save()
  return redirect("ideas:main")

def detail(req, pk):
  ideapost = IdeaPost.objects.get(id=pk)
  related_devtools = ideapost.devtools.related_ideas.all() if ideapost else []
  ctx = {'ideapost': ideapost, 'related_devtools': related_devtools}
  return render(req, 'ideaposts/detail.html', ctx)


def delete(req,pk):
  IdeaPost.objects.get(id=pk).delete()
  return redirect('ideas:main')

def update(req,pk):
  ideapost = IdeaPost.objects.get(id=pk)
  if req.method == "GET":
    ideaform = IdeaPostForm(instance=ideapost)
    ctx = {'ideaform' : ideaform, 'pk':pk}
    return render(req,'ideaposts/update.html',ctx)
  
  ideaform = IdeaPostForm(req.POST, req.FILES, instance=ideapost)
  if ideaform.is_valid():
    ideaform.save()
  return redirect("ideas:detail", pk)
