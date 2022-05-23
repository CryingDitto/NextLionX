from django.shortcuts import render, redirect
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts':posts})

@login_required(login_url='/registration/login')
def createPost(request):
    if request.method == "POST":
        newPost = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            event_time = request.POST['eventtime'],

            author = request.user,
        )
        return redirect('detail', newPost.pk)
    return render(request, 'createPost.html')


@login_required(login_url='/registration/login')
def detail(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    if request.method=="POST":
        content = request.POST['content']
        Comment.objects.create(
            post = post[0],    # 댓글 달 게시물
            content = content, # 댓글 내용
            author=request.user, # 댓글 쓴 사람
        )
        return redirect('detail', post_pk)
    else:
        # 댓글 달 때는 조회수 안 늘려주려고...
        post.update(
            numviews=post[0].numviews + 1,
        )

    return render(request, 'detail.html', {'post':post[0]})


@login_required(login_url='/registration/login')
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

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)
    

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # username 중복 불가
        found_user = User.objects.filter(username = username) # Query set 반환
        if len(found_user): # 1: 이미 해당 username 존재
            error_msg = '이미 아이디가 존재합니다!'
            return render(request, 'registration/signup.html', {'error_msg':error_msg})
        new_user = User.objects.create_user(username = username, password = password)

        # user 정보를 session에 저장해 매번 로그인하지 않게끔
        # auth.login(request, user객체): 사용자 정보를 session에 저장
        auth.login(request, new_user)
        return redirect('main')
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username = username, password=password)
        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # return redirect("main")

            # request.GET : request 데이터를 딕셔너리 형태로 변환
            # dict.get(key): 딕셔너리 함수로 키값을 가지고 데이터를 가져옴
            # next라는 키로 로그인하기 전에 들렀던 페이지로 접근함.
            # 만약 createPost.html에서 login으로 넘어왔다면
            # redirect("createPost")가 되어 로그인 후 createPost로 이동시켜줌.
            return redirect(request.GET.get('next','/'))
        error_msg = '아이디 또는 비밀번호가 틀립니다.'
        return render(request, 'registration/login.html', {'error_msg':error_msg})

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('main')