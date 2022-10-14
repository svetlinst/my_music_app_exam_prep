from django import template

from my_music_app.profiles.models import Profile

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.all().count() > 0
