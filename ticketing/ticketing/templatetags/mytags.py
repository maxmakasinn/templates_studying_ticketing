from django import template

register = template.Library()

time_format = "%A, %B, %d, %Y at %I:%M%p"
time_format_mil = "%A, %B, %d, %Y at %H:%M%p"


def my_date(old_value, miltime=False):
    if miltime:
        return old_value.strftime(time_format_mil)
    return old_value.strftime(time_format)


register.filter("my_date", my_date)
