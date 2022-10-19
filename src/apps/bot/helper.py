from src.apps.bot.models.bot_user import BotUser


def user_check_credentials(chat_id):
    obj = BotUser.objects.get_user(chat_id)
    return None not in [
                obj.first_name,
                obj.last_name,
                obj.phone_number,
            ]
