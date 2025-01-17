from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from core.models import Post, MainPost, ContentPost, Content


# Register your models here.
class PostAdmin(admin.StackedInline):
    model = Post


class ContentPostRelAdmin(admin.StackedInline):
    model = ContentPost


@admin.register(MainPost)
class MainPostAdmin(admin.ModelAdmin):
    model = MainPost
    list_display = ['title', 'foo_link', 'type_post']

    def foo_link(self, obj):
        return mark_safe(f'<a href={reverse("post_view", kwargs={"slug": obj.slug})}>{obj.title}</a>')

    foo_link.allow_tags = True
    foo_link.short_description = "foo"

    inlines = [PostAdmin, ContentPostRelAdmin]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    model = Content
    inlines = [ContentPostRelAdmin]
    list_display = ['title', 'foo_link']

    def foo_link(self, obj):
        return mark_safe(u'<a href="/فهرست/%s/">%s</a>' % (obj.slug, obj.title))
