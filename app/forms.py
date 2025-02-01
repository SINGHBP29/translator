from django import forms
from .models import FAQ
from ckeditor.widgets import CKEditorWidget

class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())  # CKEditor for formatted input

    class Meta:
        model = FAQ
        fields = ['question', 'answer']
