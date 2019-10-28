from django.db import models


class Foo(models.Model):
    value = models.CharField(max_length=20)
    another_value = models.CharField(max_length=40)
