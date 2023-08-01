# from os import major
from django.shortcuts import render, redirect
from .models import Major, Subject #내가 만든 Major라는 모델 사용
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.
# CreateView가 알아서 폼 만들어줌.
class AddMajorView(CreateView): 
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    
    #페이지가 바뀌어야 할 때 어디로 redirect 할 것인가? home
    success_url = reverse_lazy('home') 


class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'

    #페이지가 바뀌어야 할 때 어디로 redirect 할 것인가? home
    success_url = reverse_lazy('home')


class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'

    #페이지가 바뀌어야 할 때 어디로 redirect 할 것인가? home
    success_url = reverse_lazy('home')


class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'

    #페이지가 바뀌어야 할 때 어디로 redirect 할 것인가? home
    success_url = reverse_lazy('home')
    


def addMajor(request):
    if request.method == "POST":
        Major.objects.create(
            name = request.POST['name'],
        )
        return redirect('home')
    return render(request, 'addMajor.html')
        
def home(request):
    majors = Major.objects.all().order_by('name')
    subjects = Subject.objects.all().order_by('subject_name')
    return render(request, 'home.html', {'majors':majors, 'subjects':subjects,})

def computerSubjectView(request):
    # foreign key일 때 오브젝트 자체를 받아오는 것이기 때문에 __name 등으로 attribute를 지칭해줘야 함.
    computers = Subject.objects.all().filter(major__name='컴퓨터학과')
    # filtered_major = computers.major
    return render(request, 'computer.html', {'computers':computers})

def deleteSubject(request, subject_id):
    subject = Subject.objects.get(pk=subject_id).delete()
    
    return redirect('home')
    

def deleteMajor(request, major_id):
    # for subject in Subject.objects.filter(major__name=major):
    #     subject.delete()
    for subject in Subject.objects.filter(pk=major_id):
        subject.delete()
    Major.objects.get(pk=major_id).delete()
    
    return redirect('home')

def major(request, major_id):
    # subjects = Subject.objects.all().filter(major__name = major)
    major_name = Major.objects.get(pk=major_id)
    subjects = Subject.objects.all().filter(major__name = major_name)
    return render(request, 'major.html', {'subjects':subjects, 'major_name':major_name})