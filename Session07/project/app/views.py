from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    #objects에서 반환되는 것이 QuerySet
    
    return render(request, 'home.html', {'posts':posts})

def new(request):
    if request.method =='POST':
        new_post = Post.objects.create(
            # request: 브라우저가 django에 요청할 때 생기는 요청 객체
            # name이 title인 것, content인 것 받아옴.
            
            title = request.POST['title'],
            content = request.POST['content'],
        )
        # 'detail': url의 논리적인 이름, 2번째 인자: 경로 변수 
        return redirect('detail', new_post.pk)
        
    # method가 GET일 때는 if 절 실행하지 않음. 
    # 그래서 글쓰기 창 new.html로 넘어가기만 하고 새로운 게시물을 만들지는 않음.
    return render(request, 'new.html')

def detail(request, post_pk):
    # post_pk는 urls.py의 url에서 받아온 것
    post = Post.objects.get(pk=post_pk)
    
    return render(request, 'detail.html', 
                  {'post': post},  # html에서 사용하기 위한 변수. 앞에 있는 key값으로 접근한다.
                  
                  )

def edit(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    
    # update()는 QuerySet 타입에서만 사용이 가능
    # all(), filter() 이후에만 사용해야 함
    # get()은 객체 하나만 반환
    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content = request.POST['content'],
            
        )
        return redirect('detail', post_pk)
    
    return render(request, 'edit.html', {'post':post})

def delete(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    post.delete()
    
    return redirect('home') #삭제 후 home으로 이동
    
            