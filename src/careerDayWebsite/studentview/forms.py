from django import forms

class unknownWordForm(forms.Form):
    unknownWord = forms.CharField(label='')

class studentZipcode(forms.Form):
    zip_code = forms.CharField(label='')