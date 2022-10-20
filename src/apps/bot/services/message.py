from src.apps.bot.models.bot_content import BotContent
from src.apps.bot.models.bot_user import BotUser


def language_text_handler(text, chat_id):
    return all(
        [
            BotContent.objects.language_text_handler(text),
            BotUser.objects.is_going_to_edit_language(chat_id),
        ],
    )


def update_settings_language_by_text(text, chat_id):
    return all(
        [
            BotContent.objects.language_text_handler(text),
            BotUser.objects.is_going_to_edit_settings_language(chat_id),
        ],
    )


def settings_language_by_text():
    return BotContent.objects.settings_language()


def settings_back_to_menu_by_text():
    return BotContent.objects.settings_back_to_menu()


def profile_text_handler():
    return BotContent.objects.profile()


def is_going_to_edit_first_name(chat_id):
    return BotUser.objects.is_going_to_edit_first_name(chat_id)


def is_going_to_edit_last_name(chat_id):
    return BotUser.objects.is_going_to_edit_last_name(chat_id)


def is_going_to_edit_phone_number(chat_id):
    return BotUser.objects.is_going_to_edit_phone_number(chat_id)


def is_registered_first_name(chat_id):
    return BotUser.objects.is_registered_first_name(chat_id)


def is_registered_last_name(chat_id):
    return BotUser.objects.is_registered_last_name(chat_id)


def is_registered_phone_number(chat_id):
    return BotUser.objects.is_registered_phone_number(chat_id)


def is_going_to_enter_item_title(chat_id):
    return BotUser.objects.is_going_to_enter_item_title(chat_id)


def is_going_to_enter_item_location(chat_id):
    return BotUser.objects.is_going_to_enter_item_location(chat_id)


def is_going_to_enter_item_date(chat_id):
    return BotUser.objects.is_going_to_enter_item_date(chat_id)


def is_going_to_enter_item_photo(chat_id):
    return BotUser.objects.is_going_to_enter_item_photo(chat_id)


def settings_text_handler():
    return BotContent.objects.settings()


def post_item_text_handler():
    return BotContent.objects.post_item()
