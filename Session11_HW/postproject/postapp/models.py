from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    event_time = models.DateTimeField(default = timezone.now)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # 조회수
    numviews = models.PositiveIntegerField(default=0)

    # 작성자 정보
    author = models.ForeignKey(User, models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    # 댓글 작성자 정보
    author = models.ForeignKey(User, models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content
