from django.contrib import admin

from src.apps.bot.models.bot_content import BotContent
from src.apps.bot.models.bot_user import BotUser


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
