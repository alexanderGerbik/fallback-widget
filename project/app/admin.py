from django.contrib import admin
from django.forms import widgets

from app.models import Foo


@admin.register(Foo)
class FooAdmin(admin.ModelAdmin):
    pass
widgets