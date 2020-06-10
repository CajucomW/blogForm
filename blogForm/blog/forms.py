from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('username', 'text',)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'created': forms.DateField(attrs={'class': 'form-control'})
        }