"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# must import views!!!!!!!!
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # url name: views내 함수에 전달됨
    path('new', views.new, name='new'),
    path('list', views.list, name='list'),
    # path('category', views.category, name = 'category'),
    path('category/<str:article_category>', views.category, name='category'),

    # / 뒤에 들어오는 값이 article_id라는 이름으로 views.py에 전달됨
    path('detail/<int:article_id>', views.detail, name='detail'),
]
