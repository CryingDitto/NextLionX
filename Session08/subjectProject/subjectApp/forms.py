from secrets import choice
from socket import fromshare
from django import forms
from .models import Major, Subject

Major_choices = Major.objects.all().values_list('name','name')

class MajorModelForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control',
                                             'style': 'width: 300px; height: 30px; font-size:large; font-family:inherit;',
                                             'placeholder':'전공을 입력하세요.'}),
        }
        
class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('major', 'subject_name', 'prof_name', 'memo')
        widgets = {
            'major': forms.Select(choices=Major_choices, 
                                  attrs = {'class':'form-control',
                                           'style': 'font-size:large; font-family:inherit; padding:.5em 94px;',
                                        } 
                                  ),
            'subject_name': forms.TextInput(
                attrs = {'class':'form-control', 
                         'style': 'width: 300px; height: 30px; font-family:inherit; font-size:large;',
                         'placeholder':'과목명을 입력하세요.'}),
            'prof_name': forms.TextInput(
                attrs={'class':'form-control',
                       
                       'style': 'width: 300px; height: 30px; font-family:inherit; font-size:large;',
                       'placeholder': '교수님 이름을 입력하세요.'}),
            'memo':forms.TextInput(
                attrs={'class':'form-control',
                       'style': 'width: 300px; height: 30px; font-family:inherit; font-size:large;',
                       'placeholder':'메모사항을 입력하세요.'}),
            
        }