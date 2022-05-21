from django.shortcuts import render

def list_views(request):
    return render(request, 'home.html')
