
from django.contrib import admin
from .models import BlogPost, Category, Tag


# Admin Interface Configuration
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('category',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)