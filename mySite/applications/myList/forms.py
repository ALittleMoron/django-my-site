from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Product


class CKProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget,
            'opinion': CKEditorWidget
        }


class RatingOnlyAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['parent_product'].queryset = Product.objects.filter(rating__isnull=True)
    
