from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index_page"),
    path("add/", views.Add.as_view(), name="add_item"),
    path("delete/", views.Delete.as_view(), name="delete_item")
]
