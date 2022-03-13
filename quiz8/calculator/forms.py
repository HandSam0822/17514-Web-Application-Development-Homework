from re import L
from django import forms


class NumberForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()

    def clean_y(self):
        if self.cleaned_data["y"] == 0:
            raise forms.ValidationError("can't divide by zero")
        return self.cleaned_data["y"]
