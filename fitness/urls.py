from django.urls import path  # URL yönlendirmesi için gerekli modül
from . import views  # Mevcut dizindeki views modülünü içe aktarır

# URL desenlerinin listesi
# http://127.0.0.1:8000
# http://127.0.0.1:8000/fitness
# http://127.0.0.1:8000/about
# http://127.0.0.1:8000/login
# http://127.0.0.1:8000/contact

urlpatterns = [
    path("", views.index, name="home"),  # Anasayfa için URL deseni
    path("fitness", views.fitness, name="fitness"),  # Fitness sayfası için URL deseni
    path("about", views.about, name="about"),  # Hakkında sayfası için URL deseni
    path("contact", views.contact, name="contact"),  # İletişim sayfası için URL deseni
    path("login", views.login_request, name="login"),  # Giriş sayfası için URL deseni
    path("register", views.register_request, name="register"),  # Kayıt sayfası için URL deseni
    path("logout", views.logout_request, name="logout"),  # Çıkış işlemi için URL deseni
]
