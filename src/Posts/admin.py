from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    search_fields= ["Title","content"]
    list_filter=["timestamp"]
    list_display=['Title', 'timestamp', 'picture']


admin.site.register(Post, PostModelAdmin)