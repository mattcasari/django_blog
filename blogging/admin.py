from django.contrib import admin
from blogging.models import Post, Category, PostCategory

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['Post']

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)