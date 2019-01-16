from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    print(request.user)
    return HttpResponse("<h1>asdfadfs</h1>")
