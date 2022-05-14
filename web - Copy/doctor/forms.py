from django import forms
from doctor.models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["username", "password"]
