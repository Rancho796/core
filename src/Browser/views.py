from django.shortcuts import render

def indexView(request):
    return render(request,'Index.html')

def browserview(request):
    if request.method=="POST":
        
    return render(request,'Browserpage.html')
# Create your views here.
