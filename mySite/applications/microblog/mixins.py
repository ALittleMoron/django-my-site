from django.views.generic.detail import SingleObjectMixin


class NoNavbar(SingleObjectMixin):
    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['notNavigate'] = True
        return content