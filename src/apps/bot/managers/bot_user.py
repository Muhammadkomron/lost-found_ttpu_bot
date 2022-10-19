from src.apps.common.managers.common import BaseManager


class BotUserManager(BaseManager):
    def get_user(self, chat_id):
        obj = self.filter(
            chat_id=chat_id,
        ).first()
        return obj

    def get_user_by_uuid(self, user_uuid):
        qs = self.filter(
            uuid=user_uuid,
        )
        if qs.exists():
            obj = qs.first()
            return obj
        return None

    def is_going_to_edit_settings_language(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_going_to_edit_settings_language=True,
        ).exists()

    def is_going_to_edit_language(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_going_to_edit_language=True,
        ).exists()

    def is_going_to_edit_first_name(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_going_to_edit_first_name=True,
        ).exists()

    def is_going_to_edit_last_name(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_going_to_edit_last_name=True,
        ).exists()

    def is_going_to_edit_phone_number(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_going_to_edit_phone_number=True,
        ).exists()

    def is_registered_first_name(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_registered_first_name=False,
        ).exists()

    def is_registered_last_name(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_registered_last_name=False,
        ).exists()

    def is_registered_phone_number(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_registered_phone_number=False,
        ).exists()

    def is_registered_location(self, chat_id):
        return self.filter(
            chat_id=chat_id,
            is_registered_location=False,
        ).exists()
