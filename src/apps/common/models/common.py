from django.db import models


class LanguageChoice(models.TextChoices):
    ENGLISH = "🇺🇸 English", "en"
    RUSSIAN = "🇷🇺 Русский", "ru"
    UZBEK = "🇺🇿 O'zbekcha", "uz"


class StatusChoices(models.IntegerChoices):
    CREATED = 1, "Created"
    PUBLISHED = 2, "Published"
    DELIVERED = 3, "Delivered"
    CANCELLED = 4, "Cancelled"
    REJECTED = 5, "Rejected"
    BLOCKED = 6, "Blocked"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
