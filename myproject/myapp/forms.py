from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        

class Demoform(forms.Form):
    name=forms.CharField(widget=forms.Textarea(attrs={'rows':5}))

SHIFTS={
    ("1","Morning"),
    ("2","Afternoon"),
    ("3","Evening"),
}
class InputForm(forms.Form):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    shift=forms.ChoiceField(choices=SHIFTS)


