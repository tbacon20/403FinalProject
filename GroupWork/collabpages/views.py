from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) : 
    return render(request, 'classpages/index.html')

def dueDatesPageView(request) : 
    return render(request, 'classpages/duedates.html')

def IS401PageView(request) : 
    return render(request, 'classpages/is401.html')

def IS402PageView(request) : 
    return render(request, 'classpages/is402.html')

def IS403PageView(request) : 
    return render(request, 'classpages/is403.html')

def IS415PageView(request) : 
    return render(request, 'classpages/is415.html')