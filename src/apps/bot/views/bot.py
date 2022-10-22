from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from telebot import TeleBot, types

from src.apps.bot.sender import (
    start,
    admin,
    update_language,
    admin_update_language,
    enter_first_name,
    enter_last_name,
    enter_phone_number,
    admin_enter_phone_number,
    profile,
    profile_cancel,
    admin_profile_cancel,
    edit_first_name,
    update_first_name,
    edit_last_name,
    update_last_name,
    edit_phone_number,
    update_phone_number,
    update_settings,
    settings_language,
    settings_back_to_menu,
    admin_settings_back_to_menu,
    update_settings_language,
    post_item,
    post_item_title,
    post_item_location,
    post_item_date,
    post_item_photo,
    post_item_photo_exception,
    item_list,
    item_list_cancel,
    pending_item_list,
    pending_item_list_cancel,
    pending_item_reject,
    pending_item_approve,
    active_item_list,
    active_item_list_cancel,
    active_item_taken,
)
from src.apps.bot.services.bot import login
from src.apps.bot.services.message import (
    language_text_handler,
    profile_text_handler,
    settings_text_handler,
    post_item_text_handler,
    item_list_text_handler,
    pending_item_list_text_handler,
    active_item_list_text_handler,
    settings_language_by_text,
    settings_back_to_menu_by_text,
    update_settings_language_by_text,
    is_going_to_edit_first_name,
    is_going_to_edit_last_name,
    is_going_to_edit_phone_number,
    is_registered_first_name,
    is_registered_last_name,
    is_registered_phone_number,
    is_going_to_enter_item_title,
    is_going_to_enter_item_location,
    is_going_to_enter_item_date,
    is_going_to_enter_item_photo,
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
    commands=["admin"],
    func=lambda message: login(message.from_user.username),
)
def message_handler(message):
    admin(
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
    login(message.from_user.username)
    and
    language_text_handler(message.text, message.chat.id),
)
def message_handler(message):
    admin_update_language(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
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
    content_types=["contact"],
    func=lambda message:
    login(message.from_user.username)
    and
    is_registered_phone_number(message.chat.id),
)
def message_handler(message):
    admin_enter_phone_number(
        bot,
        message.contact.phone_number,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
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
    login(call.from_user.username)
    and
    "profile_cancel" == call.data,
)
def message_handler(call):
    admin_profile_cancel(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.callback_query_handler(
    func=lambda call:
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
    login(message.from_user.username)
    and
    message.text in settings_back_to_menu_by_text(),
)
def message_handler(message):
    admin_settings_back_to_menu(
        bot,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    update_settings_language_by_text(message.text, message.chat.id),
)
def message_handler(message):
    update_settings_language(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    message.text in post_item_text_handler(),
)
def message_handler(message):
    post_item(
        bot,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_enter_item_title(message.chat.id),
)
def message_handler(message):
    post_item_title(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_enter_item_location(message.chat.id),
)
def message_handler(message):
    post_item_location(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_enter_item_date(message.chat.id),
)
def message_handler(message):
    post_item_date(
        bot,
        message.text,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["photo"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_enter_item_photo(message.chat.id),
)
def message_handler(message):
    post_item_photo(
        bot,
        message.photo[-1].file_id,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["document"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    is_going_to_enter_item_photo(message.chat.id),
)
def message_handler(message):
    post_item_photo_exception(
        bot,
        message.chat.id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username).__eq__(False)
    and
    message.text in item_list_text_handler(),
)
def message_handler(message):
    item_list(
        bot,
        message.chat.id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username).__eq__(False)
    and
    "item_list#" in call.data,
)
def message_handler(call):
    item_list(
        bot,
        call.message.chat.id,
        call.message.message_id,
        int(call.data.split("#")[-1]),
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username).__eq__(False)
    and
    "item_list_cancel" == call.data,
)
def message_handler(call):
    item_list_cancel(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username)
    and
    message.text in pending_item_list_text_handler(),
)
def message_handler(message):
    pending_item_list(
        bot,
        message.chat.id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username)
    and
    "pending_item_list#" in call.data,
)
def message_handler(call):
    pending_item_list(
        bot,
        call.message.chat.id,
        call.message.message_id,
        int(call.data.split("#")[-1]),
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username)
    and
    "pending_item_list_cancel" == call.data,
)
def message_handler(call):
    pending_item_list_cancel(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username)
    and
    "pending_item_reject#" in call.data,
)
def message_handler(call):
    pending_item_reject(
        bot,
        call.message.chat.id,
        call.message.message_id,
        int(call.data.split("#")[-1]),
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username)
    and
    "pending_item_approve#" in call.data,
)
def message_handler(call):
    pending_item_approve(
        bot,
        call.message.chat.id,
        call.message.message_id,
        int(call.data.split("#")[-1]),
    )


@bot.message_handler(
    content_types=["text"],
    func=lambda message:
    login(message.from_user.username)
    and
    message.text in active_item_list_text_handler(),
)
def message_handler(message):
    active_item_list(
        bot,
        message.chat.id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username)
    and
    "active_item_list_cancel" == call.data,
)
def message_handler(call):
    active_item_list_cancel(
        bot,
        call.message.chat.id,
        call.message.message_id,
    )


@bot.callback_query_handler(
    func=lambda call:
    login(call.from_user.username)
    and
    "active_item_taken#" in call.data,
)
def message_handler(call):
    active_item_taken(
        bot,
        call.message.chat.id,
        call.message.message_id,
        int(call.data.split("#")[-1]),
    )
