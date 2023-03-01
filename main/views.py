from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def info(request):
    return render(request, 'main/info.html')

def gallery(request):
    return render(request, 'main/gallery.html')


