from django import forms
from weather.models import location

class CityForm(forms.ModelForm):
    class Meta:
        model = location
        fields = ["name"]