from django.urls import include, path

urlpatterns = [
    path(
        "",
        include(
            ("src.apps.bot.bot", "src.apps.bot.bot"),
            namespace="bot",
        ),
    ),
]
