from django.contrib import admin
from .models import Post, Comment, Example

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)

'''
@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('title','content','blank')
    empty_value_display = 'X' #아무것도 입력하지 않았을 때는 X로 표기해라

'''






