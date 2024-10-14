from account.models import Attendance
from django import forms


class TimeInForm(forms.Form):

    user_id = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control"}), required=True
    )


class TimeOutForm(forms.Form):

    user_id = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control"}), required=True
    )
