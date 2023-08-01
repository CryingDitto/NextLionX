from django.db import models

# Create your models here.
class Post(models.Model):
    # column이 어떻게 저장될지 알려주는 필드
    title = models.CharField(max_length=200) #input field와 비슷. max_length 반드시 입력.
    content = models.TextField() #textarea와 비슷.
    
    # 객체를 문자열로 변환해주는 함수
    def __str__(self):
        return self.title