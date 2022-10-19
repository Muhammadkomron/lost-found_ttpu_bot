from django.urls import path

from src.apps.bot.views import bot

urlpatterns = [
    path("", bot.UpdateBot.as_view(), name='update'),
]
