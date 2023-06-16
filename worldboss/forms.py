from django import forms
from .models import UserTimezone


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserTimezone
        fields = ['timezone']
        widgets = {
            'timezone': forms.Select(attrs={'class': 'form-control'}),
        }
