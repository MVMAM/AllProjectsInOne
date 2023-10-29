from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import Artiles


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ("title", "anons", "full_text", "date")
        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название статьи',
            }),
            "anons": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Анонс статьи',
            }),
            "full_text": Textarea(attrs={
                'class':'form-control',
                'placeholder':'Текст',
            }),
            "date": DateTimeInput(attrs={
                'class':'form-control',
            }),
        }