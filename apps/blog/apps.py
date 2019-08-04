from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'apps.blog'

    class Meta:
        verbose_name = "个人博客"
