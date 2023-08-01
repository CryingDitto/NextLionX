from django.shortcuts import render, redirect
from .models import Post


def list_page(request):
    """
    1) 모든 Post를 조회한다
    2) 조회한 Post 객체들을 “posts”라는 이름으로 list_page.html에 전달한다.
    """
    posts = Post.objects.all()

    return render(request, 'app/list_page.html', {'posts':posts,  })


def create_page(request):
    """
    1) request.method가 POST라면,
    2) Post 데이터를 생성한다. 
        2-1) 데이터 생성 시, 'title'이라는 이름의 데이터를 꺼내서 title이라는 필드에 넣고,
        2-2) 'content'라는 이름의 데이터를 꺼내서 content라는 필드에 넣는다.
    3) 데이터 생성 후에는 'detail_page'라는 이름의 url로 리다이렉트한다.  
    (detail_page로 리다이렉트하기 위해서는 해당 post의 pk값을 적절히 넘겨주어야 하겠죠)
    """
    if request.method == "POST":
        newpost = Post.objects.create(
            # request.POST에서 dictionary 형태로 넘어옴. 따라서 title, content 같은 key 값으로 조회하는 것.
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('detail_page', newpost.pk)
    return render(request, 'app/create_page.html')


def detail_page(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'app/detail_page.html', {"post": post})


def edit_page(request, post_pk):
    
    """
    1) request.method가 POST라면,
    2) post를 수정한다. 
        2-1) 수정 시, 'title'이라는 이름의 데이터를 꺼내서 title이라는 필드에 넣고,
        2-2) 'content'라는 이름의 데이터를 꺼내서 content라는 필드에 넣는다.
    3) 데이터 수정 후에는 'detail_page'라는 이름의 url로 리다이렉트한다.  
        3-1) detail_page로 리다이렉트할 때, 수정한 post 객체의 pk를 넘겨준다.
    """
    post = Post.objects.filter(pk=post_pk)
    # filter는 객체의 list 형태인 Queryset을 받아온다.
    # updata()는 Queryset의 함수이기 때문에 filter로 받아온 것.
    # 여러개의 객체를 수정 가능
    if request.method == "POST":
        post.update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        '''
        하나만 수정할 때는 단일 객체 수정 방법도 가능
        post = Post.objects.get(pk = post_pk)
        post.title = request.POST['title']
        post.content = request.POST['content']
        
        '''
        return redirect('detail_page', post_pk)
    # Queryset을 받아왔기 때문에 리스트라서 post[0] 이런 식으로 반환하는 것. 
    return render(request, 'app/edit_page.html', {'post': post[0]})



def delete(request, post_pk):
    """
    1) pk가 post_pk인 Post 객체를 조회한다.
    2) 해당 Post 객체를 지운다.
    3) 'list_page'라는 이름의 url로 리다이렉트한다.
    """
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('list_page.html')
