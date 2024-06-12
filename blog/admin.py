from django.contrib import admin
from .models import Blog,Tags,Category,Comments



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','author','date']
    search_fields=['title','author','date']

@admin.register(Tags)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','publish_at']
    search_fields=['title','publish_at']


@admin.register(Category)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','publish_at']
    search_fields=['title','publish_at']


@admin.register(Comments)
class BlogAdmin(admin.ModelAdmin):
    list_display=['name','email','blog']
    search_fields=['name','author','blog']