from django.urls import reverse
from django.views.generic import UpdateView

from app.forms import FooForm
from app.models import Foo


class UpdateFooView(UpdateView):
    model = Foo
    form_class = FooForm

    def get_success_url(self):
        return reverse('update-foo', args=[self.object.pk])
