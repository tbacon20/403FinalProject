from django.shortcuts import render
from django.http import HttpResponse
from .models import Classe, Assignment

# Create your views here.
def indexPageView(request) : 
    context = {
        "classes" : ["IS401", "IS402", "IS403", "IS415"]
    }
    return render(request, 'classpages/index.html', context)

def dueDatesPageView(request) :
    assignmentlist = [Assignment.objects.all()]
    assignments={}
    for assignment in assignmentlist:
        assignments.update({Assignment.title : Assignment.get_assignment()})
    return render(request, 'classpages/duedates.html', assignments)

def IS401PageView(request) : 
    classes = Classe.objects.all()
    return render(request, 'classpages/is401.html', {'classes': classes})

def IS402PageView(request) : 
    return render(request, 'classpages/is402.html')

def IS403PageView(request) : 
    return render(request, 'classpages/is403.html')

def IS415PageView(request) : 
    return render(request, 'classpages/is415.html')