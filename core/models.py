from django.db import models
from django.utils.text import slugify


class MainPost(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    slug = models.SlugField(allow_unicode=True, null=True, blank=True, unique=True)
    is_zyarat = models.BooleanField(default=True)
    is_not_amal = models.BooleanField(default=True)

    @property
    def type_post(self):
        if self.is_not_amal:
            if self.is_zyarat:
                return "زیارت"
            else:
                return "دعا"
        else:
            if self.is_zyarat:
                return 'اعمال'
            else:
                return "متفرقه"

    def __str__(self):
        return self.title + self.type_post

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, True)
        super(MainPost, self).save(**kwargs)


class Post(models.Model):
    sub_title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    main = models.ForeignKey("MainPost", on_delete=models.CASCADE, related_name="sub_post")


class Content(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    slug = models.SlugField(allow_unicode=True, null=True, blank=True, unique=True)
    parent = models.ForeignKey("Content", models.CASCADE, blank=True, null=True, related_name="sub_content")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, True)
        super(Content, self).save(**kwargs)

    def __str__(self):
        return self.title


class ContentPost(models.Model):
    content = models.ForeignKey("Content", on_delete=models.CASCADE, related_name="post_rel")
    post = models.ForeignKey("MainPost", on_delete=models.CASCADE, related_name="content_rel")
