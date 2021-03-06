"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from microblog.views import register, register_success

# URL Pattern is here
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # include URL pattern from microblog/urls.py
    url(r'', include('microblog.urls')),
    # Login and logout URL
    #url(r'^login/', include('django.contrib.auth.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^register/$', register),
    #url(r'^register/success/$', register_success),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
