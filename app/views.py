from pprint import pprint
from django.shortcuts import render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.db.models import Q

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
        result = get_object_or_404(MyDb, id=request.POST["id"])
        result.delete()
        return HttpResponse("Deleted successfully")


class Update(View):
    def post(self, request: WSGIRequest) -> HttpResponse:
        data = request.POST
        record = get_object_or_404(MyDb, id=data["id"])
        if len(data["username"]) != 0:
            record.username = data["username"]
        if len(data["email"]) != 0:
            record.email = data["email"]
        record.save()
        return HttpResponse("Updated Successfully")


class Search(View):
    def get(self, request:WSGIRequest) -> HttpResponse:
        try:
            query_term = request.GET["q"]
            results = MyDb.objects.filter(
                Q(username__icontains=query_term) | 
                Q(email__icontains=query_term) |
                Q(id__contains=query_term)
            )
            return render(request, "app/results.html", {
                "results": results,
                "title": "Results",
                "query": query_term
            })
        except Exception as err:
            return HttpResponseBadRequest(f"Bad request - {str(err)}")
