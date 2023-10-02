from django import template
from blog.models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe

import markdown

register = template.Library()


@register.simple_tag(name='number_of_all_published_posts')
def total_published_posts():
    return Post.published.count()


@register.inclusion_tag('blog/posts/latest_posts.html')
def show_latest_published_posts(n=3):
    latest_posts = Post.published.order_by('-publictiondate')[:n]
    return {'latest_posts': latest_posts}


@register.simple_tag()
def most_commented_published_posts(n=3):
    mc_posts = Post.published.annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:n]
    return mc_posts


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))