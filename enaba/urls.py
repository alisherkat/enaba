"""
URL configuration for enaba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path

from enaba import settings
from main import views
from main.sitemap import StaticViewSitemap, MainPostSitemap, ContentSitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'post/(?P<slug>[^/]+)/$', views.post_view, name="post_view"),
    re_path(r'content/(?P<slug>[^/]+)/$', views.content_view, name="content_view"),
    path('', views.main_page, name="main_page"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns.append(path(
    "sitemap.xml",
    sitemap,
    {"sitemaps": {"posts": MainPostSitemap,
                  'contents': ContentSitemap,
                  'main': StaticViewSitemap}},
    name="django.contrib.sitemaps.views.sitemap",
))
