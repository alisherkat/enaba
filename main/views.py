from django.shortcuts import render, get_object_or_404
from django.utils.encoding import uri_to_iri

from core.models import MainPost, Content


# Create your views here.

def post_view(request, slug):
    main_post = get_object_or_404(MainPost, slug=uri_to_iri(slug))
    title = main_post.title
    category = Content.objects.filter(parent=None).order_by('order')
    post = MainPost.objects.order_by('order')[:3]
    posts = main_post.sub_post.all()
    description = main_post.description
    if main_post.is_not_amal:
        if main_post.is_zyarat:
            color = "amber"
        else:
            color = "green"
    else:
        if main_post.is_zyarat:
            color = "slate"
        else:
            color = "purple"

    return render(request, "base_post.html",
                  {"title": title, "posts": posts, 'color': color, 'category': category, 'post': post,
                   'description': description})


def content_view(request, slug):
    content = get_object_or_404(Content, slug=uri_to_iri(slug))
    title = content.title
    category = Content.objects.filter(parent=None).order_by('order')
    post = MainPost.objects.order_by('order')[:3]
    obj = content.post_rel.order_by("post__order").all()
    objs = []
    if content.sub_content:
        for o in content.sub_content.all():
            objs.append({"title": f' فهرست{o.title}', "slug": o.slug})
    for o in obj:
        objs.append(o.post)

    color = "blue"

    return render(request, "list.html",
                  {"title": title, "objs": objs, 'color': color, 'category': category, 'post': post})


def main_page(request):
    color = "gray"
    category = Content.objects.filter(parent=None).order_by('order')
    post = MainPost.objects.order_by('order').all()[:3]
    content_zyarat = Content.objects.get(order=10)
    content_doa = Content.objects.get(order=11)
    content_amal = Content.objects.get(order=12)

    zyarat = MainPost.objects.filter(content_rel__content=content_zyarat).order_by('order')[:5]
    doa = MainPost.objects.filter(content_rel__content=content_doa).order_by('order')[:5]
    amal = MainPost.objects.filter(content_rel__content=content_amal).order_by('order')[:5]
    return render(request, 'main_page.html', {"zyarat": zyarat, "doa": doa, "amal": amal,
                                              'color': color, 'category': category, 'post': post})
