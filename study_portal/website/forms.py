from django import forms


class Logging(forms.Form):
    """ Form for inserting user account data. """
    user = forms.CharField(label='Логин', min_length=4, max_length=16, label_suffix='',
                           widget=forms.TextInput(attrs={'class': 'user'}))
    password = forms.CharField(label='Пароль', min_length=6, max_length=16, label_suffix='',
                               widget=forms.TextInput(attrs={'class': 'password'}))

