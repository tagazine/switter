from django import forms

from .models import Sweets

MAX_LENGTH = 240
class SweetForms(forms.ModelForm):
    class Meta:
        model = Sweets
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_LENGTH:
            raise forms.ValidationError("Your Sweet is too long!")
        return content
