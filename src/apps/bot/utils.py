from telebot import types

from src.apps.bot.models.bot_content import BotContent
from telegram_bot_pagination import InlineKeyboardPaginator


def language_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    languages = BotContent.objects.languages()
    keys = []
    for language in languages:
        keys.append(
            types.KeyboardButton(
                language,
            ),
        )
    keyboard.add(
        *keys,
        row_width=3,
    )
    return keyboard


def menu_keyboard(content: BotContent):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_post_item = types.KeyboardButton(content.post_item)
    key_item_list = types.KeyboardButton(content.item_list)
    key_profile = types.KeyboardButton(content.profile)
    key_settings = types.KeyboardButton(content.settings)
    keyboard.add(key_post_item)
    keyboard.add(key_item_list)
    keyboard.add(key_profile, key_settings)
    return keyboard


def admin_menu_keyboard(content: BotContent):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_pending_item_list = types.KeyboardButton(content.pending_item_list)
    key_active_item_list = types.KeyboardButton(content.active_item_list)
    key_profile = types.KeyboardButton(content.profile)
    key_settings = types.KeyboardButton(content.settings)
    keyboard.add(key_pending_item_list)
    keyboard.add(key_active_item_list)
    keyboard.add(key_profile, key_settings)
    return keyboard


def profile_keyboard(content: BotContent):
    keyboard = types.InlineKeyboardMarkup()
    key_edit_first_name = types.InlineKeyboardButton(
        text=content.first_name,
        callback_data=f"edit_first_name",
    )
    key_edit_last_name = types.InlineKeyboardButton(
        text=content.last_name,
        callback_data=f"edit_last_name",
    )
    key_edit_phone_number = types.InlineKeyboardButton(
        text=content.phone_number,
        callback_data=f"edit_phone_number",
    )
    key_cancel = types.InlineKeyboardButton(
        text=content.profile_cancel,
        callback_data=f"profile_cancel",
    )
    keyboard.add(
        key_edit_first_name,
        key_edit_last_name,
    )
    keyboard.add(
        key_edit_phone_number,
    )
    keyboard.add(
        key_cancel,
    )
    return keyboard


def contact_keyboard(content: BotContent):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_contact = types.KeyboardButton(
        content.share_phone_number,
        request_contact=True,
    )
    keyboard.add(key_contact)
    return keyboard


def settings_keyboard(content: BotContent):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_settings_language = types.KeyboardButton(
        content.settings_language,
    )
    key_back_to_menu = types.KeyboardButton(
        content.settings_back_to_menu,
    )
    keyboard.add(key_settings_language)
    keyboard.add(key_back_to_menu)
    return keyboard


def item_list_keyboard(content: BotContent, page_count, page=1):
    paginator = InlineKeyboardPaginator(
        page_count,
        current_page=page,
        data_pattern="item_list#{page}",
    )
    paginator.add_after(types.InlineKeyboardButton(content.item_list_cancel, callback_data="item_list_cancel"))
    return paginator


def pending_item_list_keyboard(content: BotContent, page_count, page=1):
    paginator = InlineKeyboardPaginator(
        page_count,
        current_page=page,
        data_pattern="pending_item_list#{page}",
    )
    paginator.add_before(
        types.InlineKeyboardButton(content.reject, callback_data=f"pending_item_reject#{page}"),
        types.InlineKeyboardButton(content.approve, callback_data=f"pending_item_approve#{page}"),
    )
    paginator.add_after(types.InlineKeyboardButton(content.item_list_cancel, callback_data="pending_item_list_cancel"))
    return paginator


def active_item_list_keyboard(content: BotContent, page_count, page=1):
    paginator = InlineKeyboardPaginator(
        page_count,
        current_page=page,
        data_pattern="active_item_list#{page}",
    )
    paginator.add_before(
        types.InlineKeyboardButton(content.taken, callback_data=f"active_item_taken#{page}"),
    )
    paginator.add_after(types.InlineKeyboardButton(content.item_list_cancel, callback_data="active_item_list_cancel"))
    return paginator
