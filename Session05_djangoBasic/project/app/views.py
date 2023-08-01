from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'hello.html')
    #request, template name을 인자로 입력