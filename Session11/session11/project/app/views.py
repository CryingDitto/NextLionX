from turtle import title
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all()

    return render(request, "home.html", {"posts": posts})


# login 한 상태여야만 글 쓸 수 있게. 로그인 안 되어 있다면 로그인 페이지로 이동시킴
@login_required(login_url="/registration/login")
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(title=title, content=content, author = request.user)
        return redirect("detail", new_post.pk)

    return render(request, "new.html")


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        return redirect("detail", post_pk)

    return render(request, "edit.html", {"post": post})

# login 해야만 게시물 세부사항 볼 수 있음
@login_required(login_url="/registration/login")
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(post=post, content=content, author = request.user)

        return redirect("detail", post_pk)
    return render(request, "detail.html", {"post": post})


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("detail", post_pk)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("home")

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        # username이 겹치지 않게끔
        # filter: queryset 반환
        found_user = User.objects.filter(username=username)
        # if len(found_user) > 0 : username 이미 존재, 0: 중복되지 않은 username
        if len(found_user): 
            error="이미 아이디가 존재합니다."
            return render(request, "registration/signup.html", {"error":error})
        new_user = User.objects.create_user(username=username, password=password)
        # user 정보를 session에 저장해야만 매번 로그인 하지 않을 수 있음
        auth.login(request, new_user)
        return redirect('home')
    return render(request, "registration/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password = password)
        if user is not None:
            auth.login(request, user, backend = "django.contrib.auth.backends.ModelBackend")
            # return redirect("home")
            # request.GET : request 데이터를 딕셔너리 형태로 변환
            # dict.get(key): 딕셔너리 함수로 키값을 가지고 데이터를 가져옴
            # next라는 키로 new라는 값에 접근함. 
            # redirect("new")가 되어 로그인 후 new 페이지로 이동시켜줌.
            return redirect(request.GET.get("next","/"))
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, "registration/login.html", {'error':error})
    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)
    return redirect("home")

