
from django.contrib import admin
from django.urls import path

from app_1.views import Index, LoginView, LogoutView, RegisterView
from app_2.views import Index2, AddView

urlpatterns = [
    # Dla app_1
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="main"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    # Dla app_2
    path('accounts/login/home/', Index2.as_view(), name="home"),
    path('add/', AddView.as_view(), name="add"),
]
