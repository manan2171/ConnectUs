from django.urls import path
from . import views
app_name = 'loginapp'

urlpatterns = [
        path('',views.home, name="home"),
        path('register/', views.register, name="register"),
        path('login/',views.login, name="login"),
]