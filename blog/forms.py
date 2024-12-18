from django import forms
from .models import Post
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib import messages

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'author']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                'tabindex': '1',
                'required': 'True',
                'autofocus': 'True'
                }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add image',
                'tabindex': '3',
                'required': 'True',
                }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author`s name',
                'tabindex': '2',
                'required': 'True'
                }),
                'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Blog Content goes here...',
                'tabindex': '4',
                'required': 'True'
                }),
        }

        def clean_text(self):
            text = self.cleaned_data.get('text')
            url_validator = URLValidator()
            words = text.split()
            urls = []
            for word in words:
                try:
                    url_validator(word)
                except ValidationError:
                    pass
                else:
                    urls.append(word)

            if urls:
                messages.warning(self.request, f"Text contains URLs: {', '.join(urls)}")

            return text
