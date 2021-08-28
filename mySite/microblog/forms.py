from django import forms
from taggit.forms import TextareaTagWidget

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "tags", "is_published")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "tags": TextareaTagWidget(attrs={'class': 'form-control'}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
