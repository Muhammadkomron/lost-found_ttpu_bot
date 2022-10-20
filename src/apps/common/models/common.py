from django.db import models


class LanguageChoice(models.TextChoices):
    ENGLISH = "🇺🇸 English", "en"
    RUSSIAN = "🇷🇺 Русский", "ru"
    UZBEK = "🇺🇿 O'zbekcha", "uz"


class StatusChoices(models.IntegerChoices):
    CREATED = 1, "Created"
    PROCESSING = 2, "Processing"
    PROCESSING_FINISHED = 3, "Processing finished"
    CANCELLED = 4, "Cancelled"
    BLOCKED = 5, "Blocked"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
