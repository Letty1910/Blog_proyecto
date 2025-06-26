from django.contrib import admin
from django.utils.html import format_html
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fecha_nacimiento', 'avatar_preview')
    search_fields = ('user__username', 'user__email')

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="40" height="40" style="object-fit: cover; border-radius: 50%;" />', obj.avatar.url)
        return "Sin imagen"

    avatar_preview.short_description = 'Avatar'