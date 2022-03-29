import random

from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    rand_number = random.randint(0, 1024)
    contex = {
        'number': rand_number,
    }
    return render(request, 'index.html', contex)


def go_to_home(request):
    return redirect('index')


def department_details(request, id):
    return HttpResponse(f'This is department {id}')


def list_departments(request):
    return HttpResponse('This is departments list')


def create_department(request):
    return HttpResponse('Created')
