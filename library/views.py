from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "home.html", context={"current_tab": "home"})


def readers(request):
    return render(request, "readers.html", context={"current_tab": "readers"})



def shop(request):
    return HttpResponse("Welcome to shopping")

def save_student(request):
    student_name = request.POST['student_name']
    return render(request, "welcome.html",context={'student_name':student_name})

