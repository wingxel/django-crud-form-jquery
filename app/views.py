from pprint import pprint
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, Http404
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
        MyDb.objects.create(username=data["username"], email=data["email"])
        return HttpResponse("Added successfully!")


class Delete(View):
    def post(self, request: WSGIRequest) -> HttpResponse:
        data = request.POST
        try:
            result = MyDb.objects.get(id=data["id"])
            result.delete()
        except MyDb.DoesNotExist:
            raise Http404(f"Item {data['id']} Not Found!")
        return HttpResponse("Deleted successfully")


class Update(View):
    def post(self, request: WSGIRequest) -> HttpResponse:
        data = request.POST
        try:
            record = MyDb.objects.get(id=data["id"])
            if len(data["username"]) != 0:
                record.username = data["username"]
            if len(data["email"]) != 0:
                record.email = data["email"]
            record.save()
        except MyDb.DoesNotExist:
            raise Http404(f"Item {data['id']} Not Found!")
        return HttpResponse("Updated Successfully")
