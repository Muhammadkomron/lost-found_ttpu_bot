from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from telebot import TeleBot, types

from src.apps.bot.sender import (
    start,
    update_language,
    enter_first_name,
    enter_last_name,
    enter_phone_number,
    profile,
    profile_cancel,
    edit_first_name,
    update_first_name,
    edit_last_name,
    update_last_name,
    edit_phone_number,
    update_phone_number,
    update_settings,
    settings_language,
    settings_back_to_menu,
    update_settings_language,
)
from src.apps.bot.services.bot import login
from src.apps.bot.services.message import (
    language_text_handler,
    profile_text_handler,
    settings_text_handler,
    settings_language_by_text,
    settings_back_to_menu_by_text,
    update_settings_language_by_text,
    is_going_to_edit_first_name,
    is_going_to_edit_last_name,
    is_going_to_edit_phone_number,
    is_registered_first_name,
    is_registered_last_name,
    is_registered_phone_number,
)

bot = TeleBot(settings.TOKEN)


class UpdateBot(APIView):
    def post(self, request):
        json_str = request.body.decode("UTF-8")
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return Response({"code": 200})


@bot.message_handler(
    commands=["start"],
    func=lambda message: login(message.from_user.username).__eq__(False),
)
def message_handler(message):
    start(
        bot,
        message.chat.id,
        message.from_user.username,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    language_text_handler(message.text, message.chat.id),
)
def message_handler(message):
    update_language(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_registered_first_name(message.chat.id),
)
def message_handler(message):
    enter_first_name(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_registered_last_name(message.chat.id),
)
def message_handler(message):
    enter_last_name(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["contact"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_registered_phone_number(message.chat.id),
)
def message_handler(message):
    enter_phone_number(
        bot,
        message.contact.phone_number,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    message.text in profile_text_handler(),
)
def message_handler(message):
    profile(
        bot,
        message.chat.id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username).__eq__(False)
    and
    "profile_cancel" == call.data,
)
def message_handler(call):
    profile_cancel(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username).__eq__(False)
    and
    "edit_first_name" == call.data,
)
def message_handler(call):
    edit_first_name(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_edit_first_name(message.chat.id),
)
def user_create_message(message):
    update_first_name(
        bot,
        message.text,
        message.chat.id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username).__eq__(False)
    and
    "edit_last_name" == call.data,
)
def message_handler(call):
    edit_last_name(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_edit_last_name(message.chat.id),
)
def user_create_message(message):
    update_last_name(
        bot,
        message.text,
        message.chat.id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username).__eq__(False)
    and
    "edit_phone_number" == call.data,
)
def message_handler(call):
    edit_phone_number(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.message_handler(
    content_types=["contact"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_edit_phone_number(message.chat.id),
)
def user_message_handler(message):
    update_phone_number(
        bot,
        message.contact.phone_number,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    message.text in settings_text_handler(),
)
def message_handler(message):
    update_settings(
        bot,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    message.text in settings_language_by_text(),
)
def message_handler(message):
    settings_language(
        bot,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    message.text in settings_back_to_menu_by_text(),
)
def message_handler(message):
    settings_back_to_menu(
        bot,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    update_settings_language_by_text(message.text, message.chat.id),
)
def message_handler(message):
    update_settings_language(
        bot,
        message.text,
        message.chat.id,
    )
