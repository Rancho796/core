from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request,'Index.html')

def browserLogin(request):
    if(request.method=="POST"):
        username=request.POST.get("username")
        email=request.POST.get("email")
        contactNo=request.POST.get("contactNo")
        password=request.POST.get("password")
        print(username,email,contactNo,password)
    return render(request,'Browserlogin.html') 
