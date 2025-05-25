from django.shortcuts import render

def main_page(request):
    return render(request, 'main_page.html')

def about_me(request):
    return render(request, 'about_me.html')

def about_project(request):
    return render(request, 'about_project.html')