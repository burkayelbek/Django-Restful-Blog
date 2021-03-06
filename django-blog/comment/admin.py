from django.contrib import admin
from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['user', 'post', 'content', 'parent', 'created']