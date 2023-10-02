from django.contrib import admin
from django.urls import path, include

from blog.views import postDetail, allPosts, postShare, postComment

app_name = 'blog'

urlpatterns = [
    # path('', ),
    path('all_posts', allPosts, name='all-posts'),
    path('tag/<slug:tag_slug>/', allPosts, name='all-posts-with-tag' ),
    # path('all_posts', PostsList.as_view(), name='all-posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', postDetail,
         name='post-detail'),
    path('<int:post_id>/share/', postShare, name='post-share'),
    path('<int:post_id>/comment/', postComment, name='post-comment'),
]
