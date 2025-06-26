from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('fecha',)