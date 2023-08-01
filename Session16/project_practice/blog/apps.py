from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog' #settings.py의 Installed Apps에 이름 들어있으면 apps.py에 들어옴. 
