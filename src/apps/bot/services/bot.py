from django.contrib.auth.models import User

from src.apps.bot.models.bot_content import BotContent
from src.apps.bot.models.bot_user import BotUser


def bot_user_create_or_update(chat_id, username):
    data = dict(
        username=username,
        is_going_to_write_message=False,
        is_going_to_edit_first_name=False,
        is_going_to_edit_last_name=False,
        is_going_to_edit_phone_number=False,
        is_going_to_edit_settings_language=False,
        is_going_to_edit_language=True,
    )
    check_user = User.objects.filter(
        username=username,
        is_active=True,
    )
    if check_user.exists():
        data.update(
            is_admin=True,
        )

    BotUser.objects.update_or_create(
        chat_id=chat_id,
        defaults=data,
    )


def bot_user_update_massage_id(chat_id, message_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.message_id = message_id
    bot_user_obj.save()


def bot_user_update_language(chat_id, language):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.language_choice = language
    bot_user_obj.is_going_to_edit_language = False
    bot_user_obj.is_going_to_edit_settings_language = False
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(language)
    return bot_user_obj, content


def bot_user_change_state(chat_id, updating_language=False):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_write_message = False
    bot_user_obj.is_going_to_edit_first_name = False
    bot_user_obj.is_going_to_edit_last_name = False
    bot_user_obj.is_going_to_edit_phone_number = False
    bot_user_obj.is_going_to_edit_settings_language = updating_language
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def bot_user_updating_first_name(chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_edit_first_name = True
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return content


def bot_user_update_first_name(message, chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_edit_first_name = False
    bot_user_obj.is_registered_first_name = True
    bot_user_obj.first_name = message
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def bot_user_updating_last_name(chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_edit_last_name = True
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return content


def bot_user_update_last_name(message, chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_edit_last_name = False
    bot_user_obj.is_registered_last_name = True
    bot_user_obj.last_name = message
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def bot_user_updating_phone_number(chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_edit_phone_number = True
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return content


def bot_user_update_phone_number(message, chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_edit_phone_number = False
    bot_user_obj.is_registered_phone_number = True
    bot_user_obj.phone_number = message
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def user_change_state(chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_write_message = False
    bot_user_obj.is_going_to_edit_first_name = False
    bot_user_obj.is_going_to_edit_last_name = False
    bot_user_obj.is_going_to_edit_phone_number = False
    bot_user_obj.save()
    return bot_user_obj


def user_writing_message(chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_write_message = True
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def login(username):
    check_user = User.objects.filter(
        username=username,
        is_active=True,
    )
    if check_user.exists():
        return True
    else:
        return False
