from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/home.html')  

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def post_list(request):
    return render(request, 'posts/post_list.html')

def project_management(request):
    return render(request, 'pages/project_management.html')

def crm(request):
    return render(request, 'pages/crm.html')

def employee_management(request):
    return render(request, 'pages/employee_management.html')

def inventory_management(request):
    return render(request, 'pages/inventory_management.html')

def learning_platform(request):
    return render(request, 'pages/learning_platform.html')

def collaboration_platform(request):
    return render(request, 'pages/collaboration_platform.html')
