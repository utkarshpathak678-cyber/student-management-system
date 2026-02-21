from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            age=age,
            course=course
        )
        return redirect('home')

    return render(request, 'students/add.html')
