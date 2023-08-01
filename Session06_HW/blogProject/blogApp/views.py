from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    
    if request.method == 'POST':
        #POST 요청으로 온 데이터 확인
        print(request.POST)
        
        #ORM 사용. Article.objects.create(내용)
        # title라는 이름으로 들어온 정보를 title에 넣고
        # content라는 이름으로 들어온 정보는 content에 넣어줘
        new_article = Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
            # date : automatically written
        )
        return redirect('list') #글 목록 페이지
    return render(request, 'new.html')



# views.py에서 전달받음
def category(request, article_category):
    samecategory = Article.objects.filter(category=article_category)
    return render(request, 'category.html',
                  {'articles': samecategory,
                   'category': article_category})
    
def list(request):
    #Get every objects from Article
    articles = Article.objects.all()
    # return render(request, 'list.html', {'articles': articles})
    
    # articles_category = Article.objects.all().values_list('category').distinct()
    articles_category = Article.objects.all().values_list('category', flat=True).distinct()
    
    articles_hobby_num = Article.objects.filter(category='Hobby').count()
    articles_Food_num = Article.objects.filter(category='Food').count()
    articles_Programming_num = Article.objects.filter(category='Programming').count()
    
    
    articles.filter(category = 'Hobby')
    return render(request, 'list.html', {'articles': articles,
                                         'articles_category': articles_category,
                                         'articles_hobby_num': articles_hobby_num,
                                         'articles_food_num': articles_Food_num,
                                         'articles_programming_num': articles_Programming_num,
                                         })



def detail(request, article_id):
    # Get object from model
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', 
                  {'article_id':article_id,
                   'article':article,
                   })
    
    