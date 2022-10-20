from django.contrib import admin

from src.apps.bot.models.bot_content import BotContent
from src.apps.bot.models.bot_user import BotUser
from src.apps.bot.models.channel import Channel
from src.apps.bot.models.item import Item


class BotContentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "language",
    )


admin.site.register(BotContent, BotContentAdmin)


class BotUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "chat_id",
        "username",
        "message_id",
        "language_choice",
    )


admin.site.register(BotUser, BotUserAdmin)


class ChannelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "url",
        "channel_id",
    )


admin.site.register(Channel, ChannelAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "location",
        "found_date",
        "user",
        "status",
    )


admin.site.register(Item, ItemAdmin)
