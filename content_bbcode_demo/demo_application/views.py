from django.views import generic


class TestView(generic.TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['text'] = ('This is an example text with '
                           '[rk:b]content bbcode example[/rk:b]')
        return context

test_view = TestView.as_view()
