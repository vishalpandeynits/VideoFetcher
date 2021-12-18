from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'channel', 'published_on']
    search_fields = ['title', 'channel', ]
    
admin.site.register(Video, VideoAdmin)