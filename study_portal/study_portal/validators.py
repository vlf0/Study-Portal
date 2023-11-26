from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.translation import ngettext


class MyDifferentValidator:
    """
    Validate condition if password contains at least one specific symbol.
    """
    @staticmethod
    def validate(password, user=None):
        if password.isalnum():
            raise ValidationError(
                _(
                    " It must contain at least one specific symbol character.",
                ),
                code="need specific symbol",
            )

    @staticmethod
    def get_help_text():
        return _('The password must contains at least one specific symbol character.')
