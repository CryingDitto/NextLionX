from django.contrib import admin

# from blogProject.blogApp.models import Aritcle
from .models import Article

# Register your models here.
admin.site.register(Article)
