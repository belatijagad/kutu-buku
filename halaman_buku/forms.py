from django import forms
from .models import Ulasan

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Ulasan
        fields = ['rating', 'comment']
