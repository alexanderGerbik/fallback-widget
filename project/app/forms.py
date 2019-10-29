from django import forms
from django.forms import widgets

from app.models import Foo
from app.widgets import FallbackSelect


class FooForm(forms.ModelForm):
    value = forms.CharField(widget=FallbackSelect(choices=(
        ('value1', 'Pre-filled 1'),
        ('value2', 'Pre-filled 2'),
    )))
    another_value = forms.CharField(widget=FallbackSelect(choices=(
        ('1', 'Some value 1'),
        ('2', 'Some value 2'),
    ), attrs={'type': 'number'}, fallback_label='Custom...'))

    class Meta:
        model = Foo
        fields = ('value', 'another_value')