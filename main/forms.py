from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'talaba': forms.Select(attrs={'class': 'form-select'}),
            'kitob': forms.Select(attrs={'class': 'form-select'}),
            'kutubxonachi': forms.Select(attrs={'class': 'form-select'}),
            'qaytargan_sana': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
        }
