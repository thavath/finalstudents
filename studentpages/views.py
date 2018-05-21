from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
	context = {}
	return render(request, 'students/index.html', context)

def students(request):
	students = Student.objects.all()
	context = { 'students' : students }
	return render(request, 'students/list_students.html', context )
