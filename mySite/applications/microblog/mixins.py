from django.views.generic.detail import SingleObjectMixin


class NotNavigate(SingleObjectMixin):
    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['notNavigate'] = True
        return content