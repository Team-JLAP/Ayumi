from django.forms import ModelForm
from django import forms
from .models import Rating

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['semester', 'rate', 'attendance', 'grade', 'comment']
        widgets = {
            'semester': forms.TextInput(attrs={'class': 'text-red-400'}),
            'rate': forms.NumberInput(attrs={'class': 'bg-blue-500'}),
        }