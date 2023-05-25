from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from .models import MyDb


def index(request: WSGIRequest) -> HttpResponse:
    my_db = MyDb.objects.all()
    return render(request, "app/index.html", {
        "user_info": my_db
    })
