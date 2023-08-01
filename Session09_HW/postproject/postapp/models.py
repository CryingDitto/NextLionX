from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    event_time = models.DateTimeField(default = timezone.now)
    # create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # 조회수
    numviews = models.PositiveIntegerField(default=0)
    
