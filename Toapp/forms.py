from django import forms
from .models import ish

class toish(forms.ModelForm):
    class Meta:
        model = ish
        fields = ['nomi', 'matn']
    