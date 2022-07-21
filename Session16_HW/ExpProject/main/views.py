from django.shortcuts import render, redirect
from .models import Post, Comment, Category

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

def new(request):
    if request.method == "POST":

        categories = Category.objects.all().values() # id, category를 key로 가지는 dictionary
        for i in range(len(categories)):
            obj = categories[i]
            if obj['category'] == request.POST['category']:
                category_id = i+1

        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = Category.objects.get(pk=category_id),
            author = request.user,
        )
        return redirect('main:detail', new_post.pk)
    

    return render(request, 'main/new.html')


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        Comment.objects.create(
            content = request.POST['content'],
            post = post,
            author = request.user,
        )
        return redirect('main:detail', post.pk)
    return render(request, 'main/detail.html', {'post': post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('main:detail', post_pk)
    return render(request, 'main/edit.html',{'post': post})

def delete(request, post_pk):
    Post.objects.get(pk=post_pk).delete()
    return redirect('main:home')

def delete_comment(request, post_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('main:detail', post_pk)



# mypage 내글 모아보기
# 실험, 알바 신청 페이지

