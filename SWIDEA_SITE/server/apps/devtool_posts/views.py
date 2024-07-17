from django.shortcuts import render, redirect
from .models import DevtoolPost
from .forms import DevtoolPostForm

def list(req):
  devtools = DevtoolPost.objects.all()
  search_txt = req.GET.get('search_txt')

  if search_txt:
    devtools = devtools.filter(name__contains = search_txt)
  ctx = {'devtools' : devtools}
  return render(req,'devtoolposts/list.html',ctx)

def create(req):
  if req.method == "GET":
    form = DevtoolPostForm
    ctx = {'form' : form}
    return render(req,'devtoolposts/create.html',ctx)
  
  form = DevtoolPostForm(req.POST)
  if form.is_valid():
    form.save()
  return redirect("devtools:list")

def detail(req, pk):
  devtool = DevtoolPost.objects.get(id=pk)

  if devtool:
    related_ideas = devtool.related_ideas.all()
  else:
    related_ideas = []

  ctx = {'devtool':devtool, 'related_ideas':related_ideas}
  return render(req,'devtoolposts/detail.html',ctx)

def delete(req, pk):
  DevtoolPost.objects.get(id=pk).delete()
  return redirect("devtools:list")

def update(req, pk):
  devtool = DevtoolPost.objects.get(id=pk)
  if req.method == "GET":
    form = DevtoolPostForm(instance=devtool)
    ctx = {'form':form, 'pk':pk}
    return render(req,'devtoolposts/update.html',ctx)
  
  form = DevtoolPostForm(req.POST, instance=devtool)
  if form.is_valid():
    form.save()

  return redirect("devtools:detail", pk)