from django.db import models

from src.apps.bot.managers.channel import ChannelManager
from src.apps.common.models.common import BaseModel


class Channel(BaseModel):
    title = models.CharField(
        max_length=255,
    )
    url = models.CharField(
        max_length=255,
    )
    channel_id = models.CharField(
        max_length=255,
    )

    objects = ChannelManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return f"{self.title}"
