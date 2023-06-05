from django.shortcuts import render

# Create your views here.
def criminal(request):
    return render(request, 'criminal.html')
