from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count

from taggit.models import Tag

from blog.forms import EmailPostForm, PostCommentForm
from blog.models import Post


# Create your views here.


def allPosts(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts_pages = paginator.page(page_number)
    except PageNotAnInteger:
        posts_pages = paginator.page(1)
    except EmptyPage:
        # return last page (num of page = last)
        posts_pages = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/posts/all-posts.html',
                  {'posts': posts_pages, 'tag': tag})


# class PostsList(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 2
#     template_name = 'blog/posts/all-posts.html'

def postDetail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLIC,
                             slug=post,
                             publictiondate__year=year,
                             publictiondate__month=month,
                             publictiondate__day=day)
    comments = post.comments.filter(active=True)
    form = PostCommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(
        id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by(
        '-same_tags', '-publictiondate')[:4]

    return render(request, 'blog/posts/post-detail.html',
                  {'post': post, 'comments': comments, 'form': form,
                   'similar_posts': similar_posts})


def postShare(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLIC)
    sent = False

    if request.method == 'GET':
        form = EmailPostForm(request.GET)
        return render(request,
                      'blog/posts/post-share.html',
                      {'post': post, 'form': form, 'sent': sent})

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["sender_name"]} send to you post {post.title} '
            msn = f"Read '{post.title}' link to {post_url}"
            send_mail(subject, msn, 'mymail@gm.com',
                      [cd['recipient_email']])
            sent = True
        else:
            form = EmailPostForm()
        return render(request,
                      'blog/posts/post-share.html',
                      {'post': post, 'form': form, 'sent': sent})


def postComment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLIC)
    comment = None
    form = PostCommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/posts/form-post-comment.html',
                  {'post': post, 'form': form, 'comment': comment})
