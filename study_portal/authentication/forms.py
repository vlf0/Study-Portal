from django import forms


class Logging(forms.Form):
    """ Form for inserting user account data. """
    user = forms.CharField(label='Логин', min_length=4, max_length=16, label_suffix='',
                           widget=forms.TextInput(attrs={'class': 'log_field'}))
    password = forms.CharField(label='Пароль', label_suffix='',  # min_length=6, max_length=16,
                               widget=forms.PasswordInput(attrs={'class': 'log_field'}))

