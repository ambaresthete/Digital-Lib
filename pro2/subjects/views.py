from django.shortcuts import render, redirect
from app2.models import Document
from .models import Watch
# Create your views here.

def Books(request):
    next = request.GET.get("next")
    print(next)
    cse=None
    ece= None
    it =None
    if next == "cse":
        cse=Document.objects.filter(department="cse",type="books")
    elif next == "ece":
        ece=Document.objects.filter(department="ece",type="books")
    elif next == "it":
        it=Document.objects.filter(department="it",type="books")
    context={
        "cse" : cse,
        "ece" : ece,
        "it" : it
    }
    return render(request,"document_list.html",context)

def Articles(request):
    next = request.GET.get("next")
    print(next)
    cse=None
    ece= None
    it =None
    if next == "cse":
        cse=Document.objects.filter(department="cse",type="articles")
    elif next == "ece":
        ece=Document.objects.filter(department="ece",type="articles")
    elif next == "it":
        it=Document.objects.filter(department="it",type="articles")
    context={
        "cse" : cse,
        "ece" : ece,
        "it" : it
    }
    return render(request,"document_list.html",context)

def Papers(request):
    next = request.GET.get("next")
    print(next)
    cse=None
    ece= None
    it =None
    if next == "cse":
        cse=Document.objects.filter(department="cse",type="papers")
    elif next == "ece":
        ece=Document.objects.filter(department="ece",type="papers")
    elif next == "it":
        it=Document.objects.filter(department="it",type="papers")
    context={
        "cse" : cse,
        "ece" : ece,
        "it" : it
    }
    return render(request,"document_list.html",context)

def cse_watch(request):
    qs = Watch.objects.filter(department="cse")
    context = {
     "object_list" : qs
    }
    return render(request,"watch.html",context)

def ece_watch(request):
    qs = Watch.objects.filter(department="ece")
    context = {
     "object_list" : qs
    }
    return render(request,"watch.html",context)

def it_watch(request):
    qs = Watch.objects.filter(department="it")
    context = {
     "object_list" : qs
    }
    return render(request,"watch.html",context)

def read(request):
    return render(request,"read.html",{})
