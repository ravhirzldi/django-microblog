from django import template
from ..models import Post
register = template.Library()

# Get total posts counts for rendering in template
@register.simple_tag
def total_post():
    return Post.published.count()