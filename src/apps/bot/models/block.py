from django.db import models

from src.apps.bot.managers.block import BlockManager
from src.apps.common.models.common import BaseModel


class Block(BaseModel):
    post = models.ForeignKey(
        "bot.Item",
        on_delete=models.CASCADE,
        related_name="blocked_items",
    )

    objects = BlockManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = "Block"
        verbose_name_plural = "Blocks"

    def __str__(self):
        return f"{self.id}"
