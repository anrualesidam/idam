from django.shortcuts import render

# Create your views here.

def homeIdam(request):
    return render(request,"home.html")