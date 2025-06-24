from django.apps import AppConfig


class NewsConfig(AppConfig):
    """
    AppConfig for the news app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
