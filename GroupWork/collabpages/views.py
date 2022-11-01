from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) : 
    return HttpResponse('Welcome Group 2-8')

def dueDatesPageView(request) : 
    return HttpResponse('Uh oh, you got stuff to do!')

def IS401PageView(request) : 
    return HttpResponse("Uh oh, you're about to be bored!")

def IS402PageView(request) : 
    return HttpResponse("Uh oh, you only have 5 minutes to finish your test!")

def IS403PageView(request) : 
    return HttpResponse('Uh oh, better be ready to google!')

def IS415PageView(request) : 
    return HttpResponse('Uh oh, better be ready to copy and paste!')