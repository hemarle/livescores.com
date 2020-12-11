from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def scores(request):

    return render(request, 'livescores/scores.html')
