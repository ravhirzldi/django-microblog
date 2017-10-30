# microblog/urls.py
from django.conf.urls import url, include
from .views import PostListView, post_detail, CreateNewPost
from . import views

urlpatterns = [
    # This is Index URL that redirect to post_list
    url(r'^$', PostListView.as_view(), name='post_list'),
    # Full Post Detail URL
    # Get 4 digits of year, 2 digits of month and day in the end is slug
    # So it will get URL like, ../2017/09/22/this-is-post
    # It will be SEO Friendly too
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    # Create new post
    url(r'^post/new/$', views.CreateNewPost.as_view(), name='post_new'),
]