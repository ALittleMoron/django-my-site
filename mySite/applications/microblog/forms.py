from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from taggit.forms import TagWidget

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "tags", "is_published")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control text-white bg-dark"}),
            "text": CKEditorUploadingWidget(attrs={"class": "form-control text-white bg-dark"}),
            "tags": TagWidget(attrs={"class": "form-control text-white bg-dark"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
