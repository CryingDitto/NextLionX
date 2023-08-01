from django.urls import path
from blog import views



app_name = 'blog'
# 중복을 피하기 위한 url 네임스페이스
urlpatterns = [
    # /blog/
    path('', views.home, name='home'), 
    path('new/', views.new, name="new"),
    path('detail/<int:post_pk>/', views.detail, name="detail"),
    path('edit/<int:post_pk>/', views.edit, name="edit"),
    path('delete/<int:post_pk>/', views.delete, name="delete"),
]
