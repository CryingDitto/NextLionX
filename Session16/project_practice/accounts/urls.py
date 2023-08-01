from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    # /accounts/
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
]
