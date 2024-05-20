from django.http import HttpResponse  # HTTP yanıtları oluşturmak için
from django.shortcuts import render, redirect  # Şablonları render etmek ve yönlendirme yapmak için
from django.contrib.auth import authenticate, login, logout  # Kullanıcı kimlik doğrulama, giriş ve çıkış işlemleri için
from django.contrib.auth.models import User  # Kullanıcı modelini kullanmak için

# Ana sayfa görünümü
def index(request):
    return render(request, "fitness/main.html")  # Ana sayfa şablonunu render eder

# Fitness sayfası görünümü
def fitness(request):
    return render(request, "fitness/fitness.html")  # Fitness sayfası şablonunu render eder

# Hakkında sayfası görünümü
def about(request):
    return render(request, "fitness/about.html")  # Hakkında sayfası şablonunu render eder

# Giriş işlemi görünümü
def login_request(request):
    if request.method == "POST":
        # Kullanıcıdan gelen bilgileri al
        username = request.POST["username"]
        password = request.POST["password"]
        # Kullanıcıyı kimlik doğrulama işlemi
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Kullanıcıyı sisteme giriş yap
            return render(request, "fitness/main.html")  # Ana sayfaya yönlendir
        else:
            return render(request, "fitness/login.html", {
                "error": "username veya parola yanlış."  # Hata mesajı göster
            })
    return render(request, "fitness/login.html")  # Giriş sayfasını render eder

# Kayıt işlemi görünümü
def register_request(request):
    if request.method == "POST":
        # Kullanıcıdan gelen bilgileri al
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmPassword")
        kvkk_check = request.POST.get("kvkkCheck")

        # Şifrelerin eşleştiğini ve KVKK onayının alındığını kontrol et
        if password != confirm_password:
            return render(request, "fitness/login.html", {
                "error": "Şifreler eşleşmiyor."  # Hata mesajı göster
            })
        else:
            if User.objects.filter(username=username).exists():
                return render(request, "fitness/login.html", {"error": "Username Kullanılıyor."})  # Hata mesajı göster
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "fitness/login.html", {"error": "E-mail Kullanılıyor."})  # Hata mesajı göster
                else:
                    # Yeni kullanıcı oluştur ve kaydet
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return render(request, "fitness/main.html")  # Ana sayfaya yönlendir

    return render(request, "fitness/login.html")  # Kayıt sayfasını render eder

# İletişim sayfası görünümü
def contact(request):
    return render(request, "fitness/contacts.html")  # İletişim sayfası şablonunu render eder

# Çıkış işlemi görünümü
def logout_request(request):
    logout(request)  # Kullanıcıyı sistemden çıkar
    return render(request, "fitness/main.html")  # Ana sayfaya yönlendir
