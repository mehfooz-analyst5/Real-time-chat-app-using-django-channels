from django.contrib import admin
from .models import ChatRoom

# Register your models here.


class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ChatRoom, ChatRoomAdmin)