from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def success(request):
    return render(request, 'main/success.html')