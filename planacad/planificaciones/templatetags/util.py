# app/templatetags/util.py
from django import template

register = template.Library()

@register.filter
def get_type(value):
    return type(value).__name__

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 

@register.filter(name='is_profesor') 
def is_profesor(user, asignatura):
    return asignatura.profesor.filter(id = user.id).exists()
