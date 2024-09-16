from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')  # Make sure 'index.html' exists in your templates folder
