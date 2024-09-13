from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    prompt = forms.CharField(max_length=500, required=True, label="Enter your custom prompt")

    class Meta:
        model = Document
        fields = ['file', 'prompt']
