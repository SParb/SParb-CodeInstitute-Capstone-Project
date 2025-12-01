from django.contrib import admin
from .models import UserPost, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(UserPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'created_on', 'approved')
    search_fields = ['title','content', 'approved']
    list_filter = ('created_on','approved')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)