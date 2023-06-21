from django.contrib import admin
from .models import MyDb


class MyDbAdmin(admin.ModelAdmin):
	list_display = ["username", "email"]


admin.site.register(MyDb, MyDbAdmin)
