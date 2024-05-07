from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request , 'root/index.html')

def details(request):
    return render(request , 'root/portfolio-details.html')