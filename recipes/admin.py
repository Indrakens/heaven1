from django.contrib import admin
from .models import Recipe, Comment


@admin.register(Recipe)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name', 'ingredients']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('name',)} 


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'cocktail', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)     
