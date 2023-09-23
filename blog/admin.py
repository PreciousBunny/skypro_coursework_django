from django.contrib import admin
from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'content')
    list_filter = ('name',)
    search_fields = ('name', 'content',)
    prepopulated_fields = {"slug": ("name",)}