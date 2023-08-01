from django.db import models
from django.urls import reverse
from accounts.models import Profile


# Create your models here.

# # Create your models here
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()

#     def __str__(self):
#         return self.title


class Post(models.Model):
    # 모델 속성 : 데이터베이스 테이블의 컬럼 = 모델 클래스의 속성 = 모델 클래스의 필드 (ORM)
    title = models.CharField(verbose_name='TITLE', max_length=50)
    # CharField는 max_length가 필수. form에서 input tag
    content = models.TextField()
    # TextField는 form에서 textarea tag
    create_dt = models.DateTimeField(auto_now_add=True)
    # auto_now_add는 생성 시각 기준으로 자동 생성
    update_dt = models.DateTimeField(auto_now=True)
    # auto_now는 저장 시각 기준으로 자동 생성
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="my_posts")
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="my_posts")
    # ForignKey는 1:N에서 N에서 설정. CASCADE가 있는 속성에 해당하는 데이터 삭제 시, 그를 포함하는 모든 객체 삭제. related_name은 역참조할 때 사용

# 메타 데이터 : 데이터에 대한 데이터. Meta 내부 클래스를 정의해 사용
    class Meta:
        verbose_name = 'post'
        # 모델 객체의 별칭.
        verbose_name_plural = 'posts'
        # 별칭의 복수형 명칭
        ordering = ('-create_dt', 'author')
        # 모델 객체 리스트 출력시 정렬 기준. -면 내림차순. 위의 경우에는 create_dt 기준으로 내림차순 후 author 기준으로 오름차순.

# 모델 메소드 : 클래스 메소드가 아니라 객체 메소드. 항상 self인자를 가지고 있으며, 테이블 단위가 아니라 레코드 단위에 영향을 미친다. (테이블 단위는 views에서 Post.objects.all() 등으로 사용)
    def __str__(self):
        # 자신(객체)의 문자열 표현을 반환한다.
        # return self.title
        return f'{self.title}입니다.'

    def get_absolute_url(self):
        # 자신(객체)의 url을 반환한다. detail을 보여주는 경우 위 메소드를 사용하면 편하다.
        return reverse(f'blog:post_detail', args=[self.id])

    # create_dt기준으로 앞 뒤 객체 반환.
    def get_previous(self):
        return self.get_previous_by_create_dt()

    def get_next(self):
        return self.get_next_by_create_dt()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="my_comments")
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="my_comments")
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_dt', 'post', 'author')

    def __str__(self):
        return f'{self.author}-{self.content}'
