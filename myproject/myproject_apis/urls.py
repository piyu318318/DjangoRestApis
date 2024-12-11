from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="homepage"),
    path('myapis/register/', views.RegisterUser.as_view(), name="Register a User "),
    path('myapis/login/', views.LoginUser.as_view(), name="login a User"),

]
