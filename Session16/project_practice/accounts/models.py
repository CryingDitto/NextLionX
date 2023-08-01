# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser # django.contrib.auth.models에서 User가 아닌 AbstractUser 더 상위 클래스를 가져왔음. 
#User는 AbstractUser를 상속하는 클래스임.

# Create your models here.


class Profile(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.PositiveIntegerField(
        help_text="User Age", blank=True, null=True)
