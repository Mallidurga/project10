from django.shortcuts import render

# Create your views here.
def app1_specific(request):
    return render(request,'app1_specific.html')