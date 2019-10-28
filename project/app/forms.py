from django import forms
from django.forms import widgets

from app.models import Foo


class FooForm(forms.ModelForm):
    value = forms.CharField(widget=widgets.TextInput())
    another_value = forms.CharField(widget=widgets.TextInput())

    class Meta:
        model = Foo
        fields = ('value', 'another_value')