from django import forms
from customer.models import Customer, Complaint_Registration, Feedback, General_Item_Order, Medicinal_Item_Order
from doctor.models import Doctor


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class UsersLoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "username", "password"


class GeneralItemOrderForm(forms.ModelForm):
    class Meta:
        model = General_Item_Order
        fields = "__all__"


class MedicinalItemOrderForm(forms.ModelForm):
    class Meta:
        model = Medicinal_Item_Order
        fields = "__all__"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"


class ComplaintRegistrationForm(forms.ModelForm):
    class Meta:
        model = Complaint_Registration
        fields = "__all__"
