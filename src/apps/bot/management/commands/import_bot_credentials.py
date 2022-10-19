from django.core.management.base import BaseCommand, CommandError

from src.apps.bot.models.bot_content import BotContent
from src.apps.bot.management.commands.bot_content_credentials import (
    bot_contents,
)


class Command(BaseCommand):
    help = "Import contents"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Importing contents... wait...",
            )
        )
        try:
            i = 0

            for bot_content in bot_contents:
                BotContent.objects.create(
                    **bot_content,
                )
                i += 1
        except FileNotFoundError:
            raise CommandError("Something went wrong!")

        self.stdout.write(
            self.style.SUCCESS(
                str(i) + "bot credentials successfully imported",
            )
        )
