from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return(HttpResponse('ererer'))
    text = 'Произвольный текст'
    return render(request,'myapp/index.html', {'text': text})