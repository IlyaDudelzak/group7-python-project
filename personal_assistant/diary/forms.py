from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'date', 'time', 'is_recurring', 'recurrence_start', 'recurrence_end']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'recurrence_start': forms.DateInput(attrs={'type': 'date'}),
            'recurrence_end': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        is_recurring = cleaned_data.get('is_recurring')
        if is_recurring:
            if not cleaned_data.get('recurrence_start') or not cleaned_data.get('recurrence_end'):
                raise forms.ValidationError("Recurring events must have start and end dates.")
        return cleaned_data