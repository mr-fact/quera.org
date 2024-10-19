from django import template

register = template.Library()


@register.filter(name='change_numbers')
def change_numbers(text):
    english_to_persian_digits = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    return ''.join(english_to_persian_digits.get(char, char) for char in text)

