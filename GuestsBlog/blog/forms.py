from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author_name', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Заголовок поста'}),
            'author_name': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Ваше ім’я'}),
            'content': forms.Textarea(attrs={'class': 'form__textarea', 'placeholder': 'Зміст...', 'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'content']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Ваше ім’я'}),
            'content': forms.Textarea(attrs={'class': 'form__textarea', 'placeholder': 'Ваш коментар', 'rows': 3}),
        }