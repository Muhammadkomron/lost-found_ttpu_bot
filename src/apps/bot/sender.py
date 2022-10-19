from django.conf import settings
from telebot.types import ReplyKeyboardRemove

from src.apps.bot.services.bot import (
    bot_user_create_or_update,
    bot_user_update_language,
    bot_user_change_state,
    bot_user_updating_first_name,
    bot_user_update_first_name,
    bot_user_updating_last_name,
    bot_user_update_last_name,
    bot_user_update_massage_id,
    bot_user_updating_phone_number,
    bot_user_update_phone_number,
)
from src.apps.bot.utils import (
    language_keyboard,
    menu_keyboard,
    profile_keyboard,
    contact_keyboard,
    settings_keyboard,
)


def start(bot, chat_id, username):
    bot_user_create_or_update(
        chat_id,
        username,
    )
    keyboard = language_keyboard()
    text = "Tilni tanlang / Выберите язык"
    response = bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    bot_user_update_massage_id(
        chat_id,
        response.message_id,
    )


def update_language(bot, language, chat_id):
    user, content = bot_user_update_language(chat_id, language)
    if not user.is_registered_first_name:
        bot.send_message(
            text=content.first_name_helper,
            chat_id=chat_id,
            reply_markup=ReplyKeyboardRemove(),
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    elif not user.is_registered_last_name:
        bot.send_message(
            text=content.last_name_helper,
            chat_id=chat_id,
            reply_markup=ReplyKeyboardRemove(),
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    elif not user.is_registered_phone_number:
        keyboard = contact_keyboard(content)
        bot.send_message(
            text=content.phone_number_helper,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    else:
        keyboard = menu_keyboard(
                content,
            )
        text = content.welcome_text
        bot.send_message(
            text=text,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )


def enter_first_name(bot, message, chat_id):
    _, content = bot_user_update_first_name(message, chat_id)
    text = content.last_name_helper
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def enter_last_name(bot, message, chat_id):
    _, content = bot_user_update_last_name(message, chat_id)
    text = content.phone_number_helper
    keyboard = contact_keyboard(
        content,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def enter_phone_number(bot, message, chat_id):
    user, content = bot_user_update_phone_number(message, chat_id)
    text = content.welcome_text
    keyboard = menu_keyboard(
        content,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def profile(bot, chat_id):
    user, content = bot_user_change_state(chat_id)
    bot.send_message(
        text=content.profile,
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    keyboard = profile_keyboard(content)
    text = f"{content.first_name_text}: {user.first_name if user.first_name else content.empty_text}\n"
    text += f"{content.last_name_text}: {user.last_name if user.last_name else content.empty_text}\n"
    text += f"{content.phone_number_text}: {user.phone_number if user.phone_number else content.empty_text}\n"
    response = bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    bot_user_update_massage_id(
        chat_id,
        response.message_id,
    )


def profile_cancel(bot, chat_id, message_id):
    _, content = bot_user_change_state(chat_id)
    text = content.profile_cancel_text
    keyboard = menu_keyboard(
        content,
    )
    bot.delete_message(
        chat_id=chat_id,
        message_id=message_id,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def edit_first_name(bot, chat_id, message_id):
    content = bot_user_updating_first_name(chat_id)
    text = content.first_name_helper
    bot.delete_message(
        chat_id=chat_id,
        message_id=message_id,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def update_first_name(bot, message, chat_id):
    user, content = bot_user_update_first_name(message, chat_id)
    keyboard = profile_keyboard(content)
    text = f"{content.first_name_text}: {user.first_name if user.first_name else content.empty_text}\n"
    text += f"{content.last_name_text}: {user.last_name if user.last_name else content.empty_text}\n"
    text += f"{content.phone_number_text}: {user.phone_number if user.phone_number else content.empty_text}\n"
    response = bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    bot_user_update_massage_id(
        chat_id,
        response.message_id,
    )


def edit_last_name(bot, chat_id, message_id):
    content = bot_user_updating_last_name(chat_id)
    text = content.last_name_helper
    bot.delete_message(
        chat_id=chat_id,
        message_id=message_id,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def update_last_name(bot, message, chat_id):
    user, content = bot_user_update_last_name(message, chat_id)
    keyboard = profile_keyboard(content)
    text = f"{content.first_name_text}: {user.first_name if user.first_name else content.empty_text}\n"
    text += f"{content.last_name_text}: {user.last_name if user.last_name else content.empty_text}\n"
    text += f"{content.phone_number_text}: {user.phone_number if user.phone_number else content.empty_text}\n"
    response = bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    bot_user_update_massage_id(
        chat_id,
        response.message_id,
    )


def edit_phone_number(bot, chat_id, message_id):
    content = bot_user_updating_phone_number(chat_id)
    text = content.phone_number_helper
    keyboard = contact_keyboard(
        content,
    )
    bot.delete_message(
        chat_id=chat_id,
        message_id=message_id,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def update_phone_number(bot, message, chat_id):
    user, content = bot_user_update_phone_number(message, chat_id)
    keyboard = profile_keyboard(content)
    text = f"{content.first_name_text}: {user.first_name if user.first_name else content.empty_text}\n"
    text += f"{content.last_name_text}: {user.last_name if user.last_name else content.empty_text}\n"
    text += f"{content.phone_number_text}: {user.phone_number if user.phone_number else content.empty_text}\n"
    bot.send_message(
        text=content.phone_number,
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    response = bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    bot_user_update_massage_id(
        chat_id,
        response.message_id,
    )


def update_settings(bot, chat_id):
    _, content = bot_user_change_state(chat_id)
    keyboard = settings_keyboard(content)
    text = content.settings
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def settings_language(bot, chat_id):
    _, content = bot_user_change_state(chat_id, updating_language=True)
    keyboard = language_keyboard()
    text = content.settings_language
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def settings_back_to_menu(bot, chat_id):
    _, content = bot_user_change_state(chat_id)
    keyboard = menu_keyboard(content)
    text = content.settings_back_to_menu
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def update_settings_language(bot, language, chat_id):
    _, content = bot_user_update_language(
        chat_id,
        language,
    )
    text = content.settings_language_text
    keyboard = settings_keyboard(
        content,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
