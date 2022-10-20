from django.db import models

from src.apps.bot.managers.item import ItemManager
from src.apps.common.models.common import BaseModel, StatusChoices


class Item(BaseModel):
    title = models.TextField(
        blank=True,
        null=True,
    )
    location = models.TextField(
        blank=True,
        null=True,
    )
    found_date = models.DateField(
        blank=True,
        null=True,
    )
    image = models.ImageField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        "bot.BotUser",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    status = models.IntegerField(
        choices=StatusChoices.choices,
        default=StatusChoices.CREATED,
    )
    message_id = models.IntegerField(
        blank=True,
        null=True,
    )

    objects = ItemManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return f"{self.title}"
