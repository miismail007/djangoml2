from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def courses(request):
    data = "this is courses page"
    return HttpResponse(data)