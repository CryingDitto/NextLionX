from django.contrib import admin
from .models import Register


# Register your models here.
# admin.site.register(Register)


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'post', 'time1',
                    'time2', 'time3', 'finalTime', 'msg')
    list_display_links = ['id', 'post']
    # id말고 제목을 눌러도 해당 글의 정보를 볼 수 있는 페이지로 이동
