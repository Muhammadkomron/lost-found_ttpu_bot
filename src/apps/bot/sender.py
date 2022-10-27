from datetime import datetime
from django.conf import settings
from telebot.types import ReplyKeyboardRemove

from src.apps.bot.models.channel import Channel
from src.apps.bot.helper import (
    get_message_photo_length_page,
    send_to_channel,
    send_notification,
)
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
    bot_user_entering_post_title,
    bot_user_entering_post_location,
    bot_user_entering_post_date,
    bot_user_entering_post_photo,
    bot_user_post_complete,
    update_item_status,
)
from src.apps.bot.utils import (
    language_keyboard,
    menu_keyboard,
    admin_menu_keyboard,
    profile_keyboard,
    contact_keyboard,
    settings_keyboard,
    item_list_keyboard,
    pending_item_list_keyboard,
    active_item_list_keyboard,
)
from src.apps.common.models.common import StatusChoices


def start(bot, chat_id, username):
    bot_user_create_or_update(
        chat_id,
        username,
    )
    keyboard = language_keyboard()
    text = "Tilni tanlang / Выберите язык / Choose language"
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


def admin(bot, chat_id, username):
    bot_user_create_or_update(
        chat_id,
        username,
    )
    keyboard = language_keyboard()
    text = "Tilni tanlang / Выберите язык / Choose language"
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


def admin_update_language(bot, language, chat_id):
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
        keyboard = admin_menu_keyboard(
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


def admin_enter_phone_number(bot, message, chat_id):
    user, content = bot_user_update_phone_number(message, chat_id)
    text = content.welcome_text
    keyboard = admin_menu_keyboard(
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


def admin_profile_cancel(bot, chat_id, message_id):
    _, content = bot_user_change_state(chat_id)
    text = content.profile_cancel_text
    keyboard = admin_menu_keyboard(
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


def admin_settings_back_to_menu(bot, chat_id):
    _, content = bot_user_change_state(chat_id)
    keyboard = admin_menu_keyboard(content)
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


def post_item(bot, chat_id):
    _, content = bot_user_entering_post_title(chat_id)
    text = content.item_title_text
    bot.send_message(
        text=content.post_item,
        chat_id=chat_id,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def post_item_title(bot, message, chat_id):
    _, content = bot_user_entering_post_location(chat_id, message)
    text = content.item_location_text
    bot.send_message(
        text=text,
        chat_id=chat_id,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def post_item_location(bot, message, chat_id):
    _, content = bot_user_entering_post_date(chat_id, message)
    text = content.item_date_text
    bot.send_message(
        text=text,
        chat_id=chat_id,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def post_item_date(bot, message, chat_id):
    try:
        date = datetime.strptime(message, "%d-%m-%Y").date()
        _, content = bot_user_entering_post_photo(chat_id, date)
        text = content.item_photo_text
        bot.send_message(
            text=text,
            chat_id=chat_id,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    except ValueError:
        _, content = bot_user_change_state(chat_id, updating_date=True)
        text = content.item_date_exception_text
        bot.send_message(
            text=text,
            chat_id=chat_id,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )


def post_item_photo(bot, file_id, chat_id):
    file_info = bot.get_file(file_id)
    file_extension = file_info.file_path.split(".")[-1]
    download_file = bot.download_file(file_info.file_path)
    user, content = bot_user_post_complete(chat_id, download_file, file_extension)
    text = content.item_create_success_text
    keyboard = menu_keyboard(
        content,
    )
    bot.send_message(
        text=text,
        chat_id=chat_id,
        reply_markup=keyboard,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    send_notification(bot, content, user)


def post_item_photo_exception(bot, chat_id):
    _, content = bot_user_change_state(
        chat_id,
        updating_photo=True,
    )
    bot.send_message(
        text=content.item_photo_exception_text,
        chat_id=chat_id,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )


def item_list(bot, chat_id, message_id=None, pk=None):
    _, content = bot_user_change_state(chat_id)
    message, photo, length, page = get_message_photo_length_page(
        pk,
        chat_id=chat_id,
    )
    if length > 0:
        if message.status == StatusChoices.CREATED:
            text = f"""{content.item_status_created_text}"""
        elif message.status == StatusChoices.PUBLISHED:
            channel_obj = Channel.objects.first()
            text = f"""{content.item_status_published_text}"""
            text = text.format(channel_obj.url + "/" + str(message.message_id))
        else:
            text = f"""{content.item_status_delivered_text}"""
        paginator = item_list_keyboard(
            content,
            page_count=length,
            page=page,
        )
        if message_id:
            bot.delete_message(
                chat_id=chat_id,
                message_id=message_id,
            )
        else:
            bot.send_message(
                text=content.item_list,
                chat_id=chat_id,
                reply_markup=ReplyKeyboardRemove(),
                parse_mode=settings.DEFAULT_PARSE_MODE,
            )
        bot.send_photo(
            photo=photo,
            caption=text,
            chat_id=chat_id,
            reply_markup=paginator.markup,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    else:
        keyboard = menu_keyboard(content)
        bot.send_message(
            text=content.item_list_exception_text,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )


def item_list_cancel(bot, chat_id, message_id):
    _, content = bot_user_change_state(chat_id)
    keyboard = menu_keyboard(content)
    text = content.item_list_cancel
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


def pending_item_list(bot, chat_id, message_id=None, pk=None):
    _, content = bot_user_change_state(chat_id)
    message, photo, length, page = get_message_photo_length_page(
        pk,
        status=StatusChoices.CREATED,
    )
    if length > 0:
        text = f"""ID: {message.id}\n"""
        text += f"""Description: {message.title}\n"""
        text += f"""Date: {message.found_date}\n"""
        text += f"""Location: {message.location}\n"""
        paginator = pending_item_list_keyboard(
            content,
            page_count=length,
            page=page,
        )
        if message_id:
            bot.delete_message(
                chat_id=chat_id,
                message_id=message_id,
            )
        else:
            bot.send_message(
                text=content.pending_item_list,
                chat_id=chat_id,
                reply_markup=ReplyKeyboardRemove(),
                parse_mode=settings.DEFAULT_PARSE_MODE,
            )
        bot.send_photo(
            photo=photo,
            caption=text,
            chat_id=chat_id,
            reply_markup=paginator.markup,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    else:
        keyboard = admin_menu_keyboard(content)
        bot.send_message(
            text=content.pending_item_list_exception_text,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )


def pending_item_list_cancel(bot, chat_id, message_id):
    _, content = bot_user_change_state(chat_id)
    keyboard = admin_menu_keyboard(content)
    text = content.pending_item_list_cancel
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


def pending_item_reject(bot, chat_id, message_id, pk):
    _, content = bot_user_change_state(chat_id)
    update_item_status(pk, StatusChoices.CREATED, StatusChoices.REJECTED)
    message, photo, length, page = get_message_photo_length_page(
        pk - 1,
        status=StatusChoices.CREATED,
    )
    if length > 0:
        text = f"""ID: {message.id}\n"""
        text += f"""Description: {message.title}\n"""
        text += f"""Date: {message.found_date}\n"""
        text += f"""Location: {message.location}\n"""
        paginator = pending_item_list_keyboard(
            content,
            page_count=length,
            page=page,
        )
        bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        bot.send_photo(
            photo=photo,
            caption=text,
            chat_id=chat_id,
            reply_markup=paginator.markup,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    else:
        keyboard = admin_menu_keyboard(content)
        bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        bot.send_message(
            text=content.pending_item_list_exception_text,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )


def pending_item_approve(bot, chat_id, message_id, pk):
    _, content = bot_user_change_state(chat_id)
    message = update_item_status(pk, StatusChoices.CREATED, StatusChoices.PUBLISHED)
    send_to_channel(bot, message)
    message, photo, length, page = get_message_photo_length_page(
        pk - 1,
        status=StatusChoices.CREATED,
    )
    if length > 0:
        text = f"""ID: {message.id}\n"""
        text += f"""Description: {message.title}\n"""
        text += f"""Date: {message.found_date}\n"""
        text += f"""Location: {message.location}\n"""
        paginator = pending_item_list_keyboard(
            content,
            page_count=length,
            page=page,
        )
        bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        bot.send_photo(
            photo=photo,
            caption=text,
            chat_id=chat_id,
            reply_markup=paginator.markup,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    else:
        keyboard = admin_menu_keyboard(content)
        bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        bot.send_message(
            text=content.pending_item_list_exception_text,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )


def active_item_list(bot, chat_id, message_id=None, pk=None):
    _, content = bot_user_change_state(chat_id)
    message, photo, length, page = get_message_photo_length_page(
        pk,
        status=StatusChoices.PUBLISHED,
    )
    if length > 0:
        text = f"""ID: {message.id}\n"""
        text += f"""Description: {message.title}\n"""
        text += f"""Date: {message.found_date}\n"""
        text += f"""Location: {message.location}\n"""
        paginator = active_item_list_keyboard(
            content,
            page_count=length,
            page=page,
        )
        if message_id:
            bot.delete_message(
                chat_id=chat_id,
                message_id=message_id,
            )
        else:
            bot.send_message(
                text=content.active_item_list,
                chat_id=chat_id,
                reply_markup=ReplyKeyboardRemove(),
                parse_mode=settings.DEFAULT_PARSE_MODE,
            )
        bot.send_photo(
            photo=photo,
            caption=text,
            chat_id=chat_id,
            reply_markup=paginator.markup,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    else:
        keyboard = admin_menu_keyboard(content)
        bot.send_message(
            text=content.active_item_list_exception_text,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )


def active_item_list_cancel(bot, chat_id, message_id):
    _, content = bot_user_change_state(chat_id)
    keyboard = admin_menu_keyboard(content)
    text = content.active_item_list_cancel
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


def active_item_taken(bot, chat_id, message_id, pk):
    _, content = bot_user_change_state(chat_id)
    update_item_status(pk, StatusChoices.PUBLISHED, StatusChoices.DELIVERED)
    message, photo, length, page = get_message_photo_length_page(
        pk - 1,
        status=StatusChoices.PUBLISHED,
    )
    if length > 0:
        text = f"""ID: {message.id}\n"""
        text += f"""Description: {message.title}\n"""
        text += f"""Date: {message.found_date}\n"""
        text += f"""Location: {message.location}\n"""
        paginator = pending_item_list_keyboard(
            content,
            page_count=length,
            page=page,
        )
        bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        bot.send_photo(
            photo=photo,
            caption=text,
            chat_id=chat_id,
            reply_markup=paginator.markup,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
    else:
        keyboard = admin_menu_keyboard(content)
        bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        bot.send_message(
            text=content.pending_item_list_exception_text,
            chat_id=chat_id,
            reply_markup=keyboard,
            parse_mode=settings.DEFAULT_PARSE_MODE,
        )
