from django.urls import path
from . import views
 #http://127.0.0.1:8000
 #http://127.0.0.1:8000/fitness
  #http://127.0.0.1:8000/about
   #http://127.0.0.1:8000/login
 #http://127.0.0.1:8000/contact

urlpatterns=[
    path("",views.index,name="home"),
    path("fitness",views.fitness,name="fitness"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("login",views.login_request,name="login"),
    path("register",views.register_request,name="register"),
    path("logout",views.logout_request,name="logout"),
    
]

