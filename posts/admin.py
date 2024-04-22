from django.contrib import admin
from .models import Post, PostFile


class PostFileInline(admin.StackedInline):
    model = PostFile
    fields = ("file",)
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'user', 'is_active', 'created_time')
    inlines = (PostFileInline,)
