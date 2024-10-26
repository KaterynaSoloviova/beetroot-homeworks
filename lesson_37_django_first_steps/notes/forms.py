from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Category, Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'reminder', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
