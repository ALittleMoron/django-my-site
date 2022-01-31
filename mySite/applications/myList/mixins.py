from django.apps import apps
from django.http.response import Http404


class ModelNameDispatchMixin:
    def dispatch(self, request, *args, **kwargs):
        model_name = kwargs.get('model_name', None)
        if not model_name:
            raise Http404
        self.model = apps.get_model(app_label='myList', model_name=model_name)
        
        return super().dispatch(request, *args, **kwargs)