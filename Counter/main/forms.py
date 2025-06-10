from django import forms

class Form1(forms.Form):
    celsius = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'celsius'}))