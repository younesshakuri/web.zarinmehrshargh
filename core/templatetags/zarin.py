from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def tr(context, obj, field):
    if obj is None:
        return ""
    return obj.translated(field, context["request"].LANGUAGE_CODE)


@register.filter
def key(mapping, name):
    if not mapping:
        return ""
    return mapping.get(name, "")
