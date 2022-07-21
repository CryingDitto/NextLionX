from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

# Create your views here.


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age','gender', 'handed', 'password1', 'password2']


def signup(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user,
                       backend="django.contrib.auth.backends.ModelBackend")
            return redirect("main:home")

        error = '아이디 또는 비밀번호가 틀립니다.'
        return render(request, 'accounts/login.html', {'error':error})
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect("main:home")
