from django import forms
from.models import Madlibs


class MadlibForm(forms.ModelForm):
    class Meta:
        model = Madlibs
        fields = ['noun', 'adjective', 'city', 'noun2', 'pronoun', 'verb', 'noun3']
