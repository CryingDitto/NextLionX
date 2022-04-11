from django.shortcuts import render, redirect
from .models import Post
from datetime import datetime

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('deadline')
    
    # to get D-day Number
    for post in posts:
        post.d_day = (post.deadline - datetime.date(datetime.now())).days
    
    return render(request, 'home.html', {'posts':posts})


def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            
            deadline = request.POST['deadline'],
            
        )
        return redirect('detail', new_post.pk)
    
    return render(request, 'new.html')
    
    
    


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    return render(request, 'detail.html', {'post': post})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method == 'POST':        
        edited_post = Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        # do not return edited_post
        # just return post_pk
        return redirect('detail', post_pk)
    
    return render(request, 'edit.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    
    return redirect('home')
