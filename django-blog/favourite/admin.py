from django.contrib import admin
from favourite.models import Favourite

@admin.register(Favourite)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('user', 'post')
    list_display = ('pk', 'user', 'post', 'content')
