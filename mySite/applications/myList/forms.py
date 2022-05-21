from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Anime, Book, Film, Game, Series


class CKAbstractAdminForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        widgets = {"description": CKEditorWidget, "opinion": CKEditorWidget}


class CKBookAdminForm(forms.ModelForm):
    class Meta(CKAbstractAdminForm.Meta):
        model = Book


class CKAnimeAdminForm(forms.ModelForm):
    class Meta(CKAbstractAdminForm.Meta):
        model = Anime


class CKFilmAdminForm(forms.ModelForm):
    class Meta(CKAbstractAdminForm.Meta):
        model = Film


class CKGameAdminForm(forms.ModelForm):
    class Meta(CKAbstractAdminForm.Meta):
        model = Game


class CKSeriesAdminForm(forms.ModelForm):
    class Meta(CKAbstractAdminForm.Meta):
        model = Series
