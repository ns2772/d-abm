from django.shortcuts import render

# Create your views here.

def HomePage(request):
    pass

def LoginPage(request):
    pass

def RepetitionPage(request):
    return render(request, 'signup.html')