from django.db import models

from src.apps.bot.managers.bot_user import BotUserManager
from src.apps.common.models.common import BaseModel, LanguageChoice


class BotUser(BaseModel):
    username = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    chat_id = models.IntegerField(
        blank=True,
        null=True,
    )
    message_id = models.IntegerField(
        blank=True,
        null=True,
    )
    language_choice = models.CharField(
        max_length=100,
        choices=LanguageChoice.choices,
        default=LanguageChoice.RUSSIAN,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_going_to_edit_language = models.BooleanField(
        default=True,
    )
    is_going_to_edit_settings_language = models.BooleanField(
        default=False,
    )
    is_going_to_enter_item_title = models.BooleanField(
        default=False,
    )
    is_going_to_enter_item_location = models.BooleanField(
        default=False,
    )
    is_going_to_enter_item_date = models.BooleanField(
        default=False,
    )
    is_going_to_enter_item_photo = models.BooleanField(
        default=False,
    )
    is_going_to_edit_first_name = models.BooleanField(
        default=False,
    )
    is_going_to_edit_last_name = models.BooleanField(
        default=False,
    )
    is_going_to_edit_phone_number = models.BooleanField(
        default=False,
    )
    is_registered_first_name = models.BooleanField(
        default=False,
    )
    is_registered_last_name = models.BooleanField(
        default=False,
    )
    is_registered_phone_number = models.BooleanField(
        default=False,
    )

    objects = BotUserManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = "Bot user"
        verbose_name_plural = "Bot users"

    def __str__(self):
        return f"{self.username}"
