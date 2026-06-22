from django import forms


class MathForm(forms.Form):

    first = forms.DecimalField()
    second = forms.DecimalField()