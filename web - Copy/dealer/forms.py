from django import forms
from dealer.models import Dealer


class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = "__all__"


class UsernLoginForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = "username", "password"
