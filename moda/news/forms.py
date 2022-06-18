from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput



class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','text','date','image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата добавления'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'image': FileInput(attrs={
                'class': 'form-control',
                'placehilder': 'Фото статьи'
            })
        }