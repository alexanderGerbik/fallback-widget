from django.forms import widgets


class FallbackSelect(widgets.Select):
    fallback_value = 'really-really-unique-value'
    template_name = 'app/widgets/fallback_select.html'
    input_type = 'text'

    class Media:
        js = ('fallback-select.js',)

    def __init__(self, fallback_label='Other...', attrs=None, choices=()):
        self.has_selected = False
        self.show_fallback = False
        if attrs is not None:
            attrs = attrs.copy()
            self.input_type = attrs.pop('type', self.input_type)
        super().__init__(attrs, choices)
        self.choices.append((self.fallback_value, fallback_label))

    def create_option(self, name, value, label, selected, index, subindex=None,
                      attrs=None):
        if index == 0:
            self.has_selected = False
            self.show_fallback = False
        self.has_selected |= selected
        if value == self.fallback_value and not self.has_selected:
            selected = True
            self.show_fallback = True
        return super().create_option(name, value, label, selected, index, subindex, attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['type'] = self.input_type
        context['show_fallback'] = self.show_fallback
        context['fallback_value'] = self.fallback_value
        return context