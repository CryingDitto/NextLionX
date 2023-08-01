from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
# Create your views here.

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts':posts})

def createPost(request):
    if request.method == "POST":
        newPost = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            event_time = request.POST['eventtime'],
            
        )
        return redirect('detail', newPost.pk)
    return render(request, 'createPost.html')

def detail(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    post.update(
        numviews = post[0].numviews + 1
    )
    return render(request, 'detail.html', {'post':post[0]})


def editPost(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    
    if request.method == "POST":
        post.update(
            title = request.POST['title'],
            content = request.POST['content'],
            event_time = request.POST['eventtime'],
            update_date = timezone.now()
        )

        
        return redirect('detail', post_pk)

    # filter -> Query set 리스트로 받아오므로 indexing 필요
    return render(request, 'editPost.html', {'post': post[0]})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('main')