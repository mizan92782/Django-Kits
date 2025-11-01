from atexit import register
from django import template


register = template.Library()

@register.filter(name='print_name')
def print_name(value):
    return f'Student name : Md {value}'

@register.filter(name='love')
def love(boy,girl):
    return f'{boy} loves {girl}'


@register.filter(name='summetation')
def summetation(boy,*args):
    return f'{boy} loves {args}'