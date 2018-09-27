from django.shortcuts import render


# Create your views here.

def ola_mundo(request):
    return render(request, 'ola_mundo.html', {})
