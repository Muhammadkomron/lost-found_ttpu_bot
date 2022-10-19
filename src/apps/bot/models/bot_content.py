from django.db import models

from src.apps.common.models.common import LanguageChoice
from src.apps.bot.managers.bot_content import BotContentManager


class BotContent(models.Model):
    language = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    profile = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    profile_cancel = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    settings = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    settings_language = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    settings_back_to_menu = models.CharField(
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
    share_phone_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    welcome_text = models.TextField(
        blank=True,
        null=True,
    )
    menu_text = models.TextField(
        blank=True,
        null=True,
    )
    first_name_text = models.TextField(
        blank=True,
        null=True,
    )
    last_name_text = models.TextField(
        blank=True,
        null=True,
    )
    phone_number_text = models.TextField(
        blank=True,
        null=True,
    )
    settings_language_text = models.TextField(
        blank=True,
        null=True,
    )
    first_name_helper = models.TextField(
        blank=True,
        null=True,
    )
    last_name_helper = models.TextField(
        blank=True,
        null=True,
    )
    phone_number_helper = models.TextField(
        blank=True,
        null=True,
    )
    profile_cancel_text = models.TextField(
        blank=True,
        null=True,
    )
    empty_text = models.TextField(
        blank=True,
        null=True,
    )
    language_choice = models.CharField(
        max_length=100,
        choices=LanguageChoice.choices,
        default=LanguageChoice.RUSSIAN,
    )

    objects = BotContentManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = "Bot content"
        verbose_name_plural = "Bot contents"

    def __str__(self):
        return f"{self.language}"
