from django import forms
from .models import Jacket

class JacketForm(forms.ModelForm):
    class Meta:
        model = Jacket
        fields = ['typ', 'color']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }
