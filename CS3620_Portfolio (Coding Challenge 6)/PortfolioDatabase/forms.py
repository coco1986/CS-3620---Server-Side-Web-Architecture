from django import forms
from .models import Portfolio, Contact


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_name', 'portfolio_desc', 'portfolio_image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['c_name', 'c_email', 'c_message']
