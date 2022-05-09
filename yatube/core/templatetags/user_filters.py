from django import template
# В template.Library зарегистрированы все встроенные теги и фильтры шаблонов;
# добавляем к ним и наш фильтр.
register = template.Library()


@register.filter 
def addclass(field, css):
    return field.as_widget(attrs={'class': css})

# синтаксис @register... , под который описана функция addclass() - 
# это применение "декораторов", функций, меняющих поведение функций
# Не бойтесь соб@к 