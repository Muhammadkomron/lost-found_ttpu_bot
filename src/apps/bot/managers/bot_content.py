from src.apps.common.managers.common import BaseManager


class BotContentManager(BaseManager):
    def language_text_handler(self, text):
        return text in self.values_list(
            "language",
            flat=True,
        )

    def languages(self):
        return self.values_list(
            "language",
            flat=True,
        )

    def settings_language(self):
        return self.values_list(
            "settings_language",
            flat=True,
        )

    def settings_back_to_menu(self):
        return self.values_list(
            "settings_back_to_menu",
            flat=True,
        )

    def profile(self):
        return self.values_list(
            "profile",
            flat=True,
        )

    def settings(self):
        return self.values_list(
            "settings",
            flat=True,
        )

    def fetch_by_language(self, language):
        return self.filter(
            language=language,
        ).first()
