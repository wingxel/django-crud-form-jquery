from pprint import pprint
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views import View

from .models import MyDb


def index(request: WSGIRequest) -> HttpResponse:
    my_db = MyDb.objects.all()
    return render(request, "app/index.html", {
        "user_info": my_db
    })


class Add(View):
    def post(self, request: WSGIRequest) -> HttpResponse:
        data = request.POST
        pprint(data)
        MyDb.objects.create(username=data["username"], email=data["email"])
        return HttpResponse("Added successfully!")
