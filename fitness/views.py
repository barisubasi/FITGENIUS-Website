from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"fitness/main.html")

def fitness(request):
  return render(request,"fitness/fitness.html")

def about(request):
   return render(request,"fitness/about.html")

def login_request(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,"fitness/main.html")
        else:
            return render(request,"fitness/login.html",{
                "error":"username veya parola yanlış."
            })
        
    return render(request,"fitness/login.html")

def register_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmPassword")
        kvkk_check = request.POST.get("kvkkCheck")

        # Şifrelerin eşleştiğini ve KVKK onayının alındığını kontrol et
        if password != confirm_password:
            return render(request, "fitness/login.html", {
                "error": "Şifreler eşleşmiyor."
            })
        else:
            if User.objects.filter(username=username).exists():
                return render(request,"fitness/login.html",{"error":"Username Kullanılıyor."})
            else:
                if User.objects.filter(email=email).exists():
                     return render(request,"fitness/login.html",{"error":"E-mail Kullanılıyor."})
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return render(request,"fitness/main.html")
 

    return render(request, "fitness/login.html")

def contact(request):
    return render(request,"fitness/contacts.html")

def logout_request(request):
    logout(request)
    return render(request,"fitness/main.html")