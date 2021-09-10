from django import forms
from taggit.forms import TextareaTagWidget, TagWidget

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "tags", "is_published")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control text-white bg-dark"}),
            "text": forms.Textarea(attrs={"class": "form-control text-white bg-dark"}),
            "tags": TagWidget(attrs={'class': 'form-control text-white bg-dark'}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
