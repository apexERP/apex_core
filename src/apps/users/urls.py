from django.urls import path

from .views import login_page, logout_page, register_page, profile_page

app_name = 'apps.users'

urlpatterns = [
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),
    path("register/", register_page, name="register"),
    path("profile/", profile_page, name="profile"),
]