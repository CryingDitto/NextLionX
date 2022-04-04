from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
# #DB에 Article 생성
# Article.objects.create(
#     title = "좋은날", 
#     content = "눈물이 차 올라서 고갤 들어",)
# Article.objects.all() #DB의 모든 Article 조회
# Article.object.get(pk=3) #pk가 3인 Article 조회

# Article.objects.create(
#     title = "Python",
#     category = 'Programming',
#     content = 'python python snake',
# )
# Article.objects.create(
#     title="Steak",
#     category='Food',
#     content='Marinated steak',
# )
# Article.objects.create(
#     title="Ditto",
#     category='Hobby',
#     content='Where are you Ditto I wanna find you someday...',
# )
