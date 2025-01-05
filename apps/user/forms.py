
from django import forms

from apps.user.models import UserAccount
from allauth.account.models import EmailAddress

class CustomEmailForm(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=UserAccount.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='id',
        label='User Account',
        help_text='Select user account',
        error_messages={
            'required': 'Please select user account',
        },
    )

    class Meta:
        model = EmailAddress
        fields = '__all__'