import uuid
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import ContentFile

from src.apps.bot.models.bot_content import BotContent
from src.apps.bot.models.bot_user import BotUser
from src.apps.bot.models.item import Item


def bot_user_create_or_update(chat_id, username):
    data = dict(
        username=username,
        is_going_to_enter_item_title=False,
        is_going_to_enter_item_location=False,
        is_going_to_enter_item_date=False,
        is_going_to_enter_item_photo=False,
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


def bot_user_change_state(chat_id, updating_language=False, updating_date=False):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_write_message = False
    bot_user_obj.is_going_to_edit_first_name = False
    bot_user_obj.is_going_to_edit_last_name = False
    bot_user_obj.is_going_to_edit_phone_number = False
    bot_user_obj.is_going_to_enter_item_title = False
    bot_user_obj.is_going_to_enter_item_location = False
    bot_user_obj.is_going_to_enter_item_date = updating_date
    bot_user_obj.is_going_to_enter_item_photo = False
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


def bot_user_entering_post_title(chat_id):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_enter_item_title = True
    bot_user_obj.is_going_to_enter_item_location = False
    bot_user_obj.is_going_to_enter_item_date = False
    bot_user_obj.is_going_to_enter_item_photo = False
    bot_user_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def bot_user_entering_post_location(chat_id, message):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_enter_item_location = True
    bot_user_obj.is_going_to_enter_item_title = False
    bot_user_obj.save()
    Item.objects.create(
        title=message,
        user=bot_user_obj,
    )
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def bot_user_entering_post_date(chat_id, message):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_enter_item_date = True
    bot_user_obj.is_going_to_enter_item_location = False
    bot_user_obj.save()
    bot_user_item_obj = bot_user_obj.posts.first()
    bot_user_item_obj.location = message
    bot_user_item_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def bot_user_entering_post_photo(chat_id, message):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_enter_item_photo = True
    bot_user_obj.is_going_to_enter_item_date = False
    bot_user_obj.save()
    bot_user_item_obj = bot_user_obj.posts.first()
    bot_user_item_obj.found_date = message
    bot_user_item_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def bot_user_post_complete(chat_id, photo, extension):
    bot_user_obj = BotUser.objects.get_user(chat_id)
    bot_user_obj.is_going_to_enter_item_photo = False
    bot_user_obj.save()
    bot_user_item_obj = bot_user_obj.posts.first()
    bot_user_item_obj.image = File(
        ContentFile(photo, f"{uuid.uuid4()}.{extension}"),
    )
    bot_user_item_obj.save()
    content = BotContent.objects.fetch_by_language(
        bot_user_obj.language_choice,
    )
    return bot_user_obj, content


def update_item_status(pk, from_status, to_status):
    obj = Item.objects.get_item_by_pk(pk, from_status)
    obj.status = to_status
    obj.save()
    return obj


def login(username):
    check_user = User.objects.filter(
        username=username,
        is_active=True,
    )
    if check_user.exists():
        return True
    else:
        return False