from django.shortcuts import render,redirect
from .models import User,Blogs

# Create your views here.
def indexView(request):
    title="abc"
    description="nothing"
    Blogs=(title=title,description=description).save()
    return render(request,"index.html")

def createUser(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        city=request.POST.get("city")
        email=request.POST.get("email") 
        password=request.POST.get("password")
        print(name,city,email,password)
        user=User()
        user.name=name
        user.email=email
        user.password=password
        user.city=city
        user.save()
        return redirect("/")
    return render(request,"createuser.html")
