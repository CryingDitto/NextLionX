from django.db import models
# django.contrib.auth.models에서 User가 아닌 AbstractUser 더 상위 클래스를 가져왔음.
from django.contrib.auth.models import AbstractUser
#User는 AbstractUser를 상속하는 클래스임.

# Create your models here.


class Profile(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=30, null=False)
    
    age = models.PositiveIntegerField(
        help_text="User Age", blank=True, null=True)
    gender = models.CharField(max_length=10)
    handed = models.CharField(max_length=10)


