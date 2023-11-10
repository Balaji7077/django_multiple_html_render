from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def abc(request):
    return render(request,'abc.html')

def mno(request):
    return render(request,'mno.html')