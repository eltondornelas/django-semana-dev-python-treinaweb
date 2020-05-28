from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

# recebe um input e a classe;
# depois adiciona nesse input a classe
# form_task.title é o input nesse caso
