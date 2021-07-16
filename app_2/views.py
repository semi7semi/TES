from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User

class Index2(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {
            "hello": "TREND ENERGY SOLUTIONS S.A. APP_2",
            "users": users
        }
        return render(request, "index2.hgittml", ctx)