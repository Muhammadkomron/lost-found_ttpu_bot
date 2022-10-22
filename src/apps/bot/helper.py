from django.conf import settings

from src.apps.bot.models.bot_user import BotUser
from src.apps.bot.models.channel import Channel
from src.apps.bot.models.item import Item
from src.apps.common.models.common import StatusChoices


def user_check_credentials(chat_id):
    obj = BotUser.objects.get_user(chat_id)
    return None not in [
                obj.first_name,
                obj.last_name,
                obj.phone_number,
            ]


def get_message_photo_length_page(pk=None, status=None):
    if status:
        pk_list = list(
            Item.objects.filter(
                status=status,
            ).values_list(
                "id",
                flat=True,
            )
        )
    else:
        pk_list = list(
            Item.objects.exclude(
                status=StatusChoices.BLOCKED,
            ).values_list(
                "id",
                flat=True,
            )
        )
    length = len(pk_list)
    if pk and length > 0:
        obj, photo = Item.objects.get_item_photo(pk_list[pk - 1])
        return obj, photo, length, pk_list.index(obj.id) if length == 1 else pk_list.index(obj.id) + 1
    if length == 0:
        return None, None, length, 1
    if not status:
        obj, photo = Item.objects.get_first_item()
    else:
        obj, photo = Item.objects.get_first_item_by_status(status)
    return obj, photo, length, pk_list.index(obj.id) + 1


def send_to_channel(bot, message):
    channel_obj = Channel.objects.first()
    obj, photo = Item.objects.get_item_photo(message.id)
    text = f"""Title: {obj.title}\n"""
    text += f"""Location: {obj.location}\n"""
    text += f"""Date: {obj.found_date}"""
    response = bot.send_photo(
        photo=photo,
        caption=text,
        chat_id=channel_obj.channel_id,
        parse_mode=settings.DEFAULT_PARSE_MODE,
    )
    obj.message_id = response.message_id
    obj.save()
