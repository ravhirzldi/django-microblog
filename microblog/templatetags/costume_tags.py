from django import template
from ..models import Post
from django.contrib.auth.models import User
import datetime, pytz
register = template.Library()

# Get total posts counts for rendering in template
@register.simple_tag
def total_post():
    return Post.published.count()

@register.simple_tag
def total_user():
    return User.objects.count()

@register.filter(name='time_since')
def time_since(date, default="just now"):
    now = datetime.datetime.utcnow().replace(tzinfo = pytz.utc)
    diff = now - date
    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )
    for period, singular, plural in periods:
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)
    return default