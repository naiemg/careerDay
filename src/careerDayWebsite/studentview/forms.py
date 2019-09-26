from django import forms

class unknownWordForm(forms.Form):
    unknownWord = forms.CharField(label='')