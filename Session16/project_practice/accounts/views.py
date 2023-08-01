from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password1', 'password2']


def signup(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
    return render(request, 'accounts/signup.html', {'form': form})
