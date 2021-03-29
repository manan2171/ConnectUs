from django.urls import path
from .views import *
app_name = "account"
urlpatterns = [
    path('register/', register_view, name = "register"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('', home_view , name = "home_page"),
    path('profile/<user_id>/', profile_view , name = "profile_page"),
    path('search_result/',search_view_result, name = "search_result"),
    path('profile/<user_id>/edit',edit_account_view, name = "edit_profile")
]