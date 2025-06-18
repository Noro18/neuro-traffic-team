from django.shortcuts import render

# Create your views here.

def monitorApp(request):
    return render(request, 'home_page.html')
