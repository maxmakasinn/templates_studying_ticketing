from django import template

register = template.Library()

time_format = "%A, %B, %d, %Y at %I:%M%p"


def my_date(old_value):
    return old_value


register.filter("my_date", my_date)
