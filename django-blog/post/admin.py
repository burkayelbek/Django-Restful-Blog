from django.contrib import admin
from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('pk', 'title', 'created', 'modified')
