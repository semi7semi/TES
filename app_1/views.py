from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView
from datetime import datetime
from django.contrib.auth.models import User
from app_1.forms import LogForm, RegisterUserForm


class Index(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {
            "hello": "Witaj na stronie TREND ENERGY SOLUTIONS S.A.",
            "users": users
        }
        return render(request, "index.html", ctx)

class LoginView(FormView):
    # logowanie i authentykacja
    form_class = LogForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, "Zły login lub haslo")
        return super().form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("main")


class RegisterView(View):
    def get(self, request):
        form = RegisterUserForm()
        ctx = {"form": form}
        return render(request, "register.html", ctx)
    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.username = user.email
            user.save()
        return redirect("main")