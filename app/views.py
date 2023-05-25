from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


def index(request: WSGIRequest) -> HttpResponse:
    return render(request, "app/index.html")
