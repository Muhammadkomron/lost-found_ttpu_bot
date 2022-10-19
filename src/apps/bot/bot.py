from django.urls import include, path

app_name = "bot"

urlpatterns = [
    path(
        "",
        include(
            (
                "src.apps.bot.urls.bot",
                "src.apps.bot.urls.bot",
            ),
            namespace="bot",
        ),
    ),
]
