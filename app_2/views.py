from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from app_2.forms import CompanyForm, SearchForm
from app_2.models import Companies


class Index2(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.all()
        form = SearchForm()
        data = Companies.objects.all()
        ctx = {
            "hello": "TREND ENERGY SOLUTIONS S.A. APP_2",
            "users": users,
            "data": data,
            "form": form
        }
        return render(request, "index2.html", ctx)
    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            date_from = form.cleaned_data["date_from"]
            date_to = form.cleaned_data["date_to"]
            if not date_from and not date_to:
                data = Companies.objects.filter(name=name)
            elif not date_from:
                data = Companies.objects.filter(name=name).filter(date__lte=date_to)
            elif not date_to:
                data = Companies.objects.filter(name=name).filter(date__gte=date_from)
            else:
                data = Companies.objects.filter(name=name).filter(date__lte=date_to).filter(date__gte=date_from)
            ctx = {
                "data": data.order_by("date")
            }
            return render(request, "list.html", ctx)



class AddView(View):
    def get(self, request):
        users = User.objects.all()
        form = CompanyForm()
        data = Companies.objects.all()
        ctx = {
            "hello": "TREND ENERGY SOLUTIONS S.A. APP_2",
            "users": users,
            "data": data,
            "form": form
        }
        return render(request, "add.html", ctx)
    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            date = form.cleaned_data["date"]
            Companies.objects.create(
                name = name,
                price = price,
                date = date
            )
            return redirect("home")