from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
admin.site.register(Category)


class CommentInline(admin.TabularInline):
    # TabularInline은 같은 admin page에서 다른 model을 수정할 수 있는 권한을 부여한다.
    model = Comment


class CategoryInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
# 데코레이터. admin.site.register(Post,PostAdmin)와 동일하다.
class PostAdmin(admin.ModelAdmin):
    # admin에서 아이디, 제목, 작성자, 작성시각이 보이게 설정함.
    # 카테고리로 필터 가능
    # 게시글에 딸려있는 이미지와 댓글을 접근 가능하도록 설정하였음.
    list_display = ['id', 'category', 'title', 'author', 'created_dt']
    # 각 객체들이 위 순서로 보이게 설정
    list_display_links = ['id', 'title']
    # id말고 제목을 눌러도 해당 글의 정보를 볼 수 있는 페이지로 이동
    list_filter = ['created_dt', 'author', 'category']
    # create_dt와 author를 기준으로 필터 생성
    search_fields = ['title', 'author', 'category']
    # title과 author, category를 검색 가능
    inlines = [
        CommentInline, CategoryInline,
    ]
    # 이제 Post 모델에서 연관된 Comment를 확인 및 수정할 수 있다.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'content', 'author')
