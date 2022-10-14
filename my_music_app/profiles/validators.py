from django.core.exceptions import ValidationError


def validate_username_characters(value):
    check_value = str(value)
    for c in check_value:
        if not c.isalnum() or c == '_':
            raise ValidationError(f'Ensure this value contains only letters, numbers, and underscore.')
