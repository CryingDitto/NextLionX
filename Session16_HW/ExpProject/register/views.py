from django.shortcuts import render, redirect
from main.models import Post
from accounts.models import Profile
from .models import Register

# Create your views here.

# 실험, 알바 신청 페이지


def enroll(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    user = Profile.objects.get(pk=request.user.pk)

    if request.method == "POST":
        regi = Register.objects.create(
            post=post,
            person=request.user,
            time1=request.POST['time1'],

            time2= request.POST['time1'],
            time3=request.POST['time3'],
            msg = request.POST['msg'],
        )

        # if request.POST['time2']:
        #     regi.time2 = request.POST['time2']
        # if request.POST['time3']:
        #     regi.time2 = request.POST['time3']
        # if request.POST['msg']:
        #     regi.msg = request.POST['msg']
        return redirect('accounts:mypage')

    return render(request, 'register/enroll.html', {'post': post})

def confirm(request, post_pk, enroll_pk):
    enroll = Register.objects.filter(pk = enroll_pk)

    if request.method == "POST":

        enroll.update(

            finalTime=request.POST["finalTime"]

        )
        return redirect('main:detail', post_pk)

    return render(request, 'register/confirm.html', {'enroll':enroll[0]})