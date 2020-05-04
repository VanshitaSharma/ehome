from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/',views.about,name="about"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('search/',views.search,name="search"),

]
