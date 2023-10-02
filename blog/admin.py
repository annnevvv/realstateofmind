from django.contrib import admin

from blog.models import Post, PostComment


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'slug', 'publictiondate', 'status']
    list_filter = ['author', 'title', 'status', 'publictiondate',
                   'creationeddate', 'updateddate', 'visible', 'status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publictiondate'
    ordering = ['status', 'publictiondate']


@admin.register(PostComment)
class PostsComment(admin.ModelAdmin):
    list_display = ['updated', 'created', 'email', 'post']
    list_filter = ['active']
    search_fields = ['post', 'email', 'created', 'updated', 'cmnt_tet']
