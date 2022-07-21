from operator import truediv
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from accounts.models import Profile

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.category
    
# class Tag(models.Model):
#     tag = models.CharField(max_length=20, null=False)
    
class Post(models.Model):
    title = models.CharField(max_length=300, null = False)
    content = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    # max_register = models.PositiveSmallIntegerField()
    author = models.ForeignKey(
           Profile, on_delete=models.CASCADE, related_name="my_posts")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="post")
    # tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    # 메타 데이터 : 데이터에 대한 데이터. Meta 내부 클래스를 정의해 사용
    class Meta:
        verbose_name = 'post'        # 모델 객체의 별칭.
        verbose_name_plural = 'posts'        # 별칭의 복수형 명칭
        
        # 모델 객체 리스트 출력시 정렬 기준. -: 내림차순.
        ordering = ('-created_dt', 'author') # created_dt 기준으로 내림차순 후 author 기준으로 오름차순.

        



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="my_comments")
    content = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_dt', 'post', 'author')

    def __str__(self):
        return f'{self.author}-{self.content}'
