from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "ninjagold_app/index.html")

def process(request):

    return redirect("/")
