from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Post, Comment, UserProfile
from .forms import CommentForm, PostForm
import json

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'pirostagram/index.html', {'posts': posts})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main:index')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'pirostagram/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'pirostagram/post_new.html', ctx)
    
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('main:post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'pirostagram/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    posts = user.posts.all().order_by('-created_at')
    return render(request, 'pirostagram/user_profile.html', {'profile': profile, 'posts': posts})

@csrf_exempt
def like_post(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']

    post = Post.objects.get(id=post_id)

    if button_type == 'like':
        post.like += 1
    else:
        post.dislike += 1

    post.save()

    return JsonResponse({'id': post_id, 'type': button_type})
