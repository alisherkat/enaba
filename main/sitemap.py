from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from core.models import MainPost, Content


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = "weekly"

    def items(self):
        return ["main_page"]

    def location(self, item):
        return reverse(item)


class MainPostSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return MainPost.objects.all()

    def location(self, item):
        return reverse("post_view", kwargs={'slug': item.slug})


class ContentSitemap(Sitemap):
    priority = 0.3
    changefreq = "monthly"

    def items(self):
        return Content.objects.all()

    def location(self, item):
        return reverse("content_view", kwargs={'slug': item.slug})
