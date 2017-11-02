from django import template
from ..models import Post
from django.contrib.auth.models import User
register = template.Library()

# Get total posts counts for rendering in template
@register.simple_tag
def total_post():
    return Post.published.count()

@register.simple_tag
def total_user():
    return User.objects.count()