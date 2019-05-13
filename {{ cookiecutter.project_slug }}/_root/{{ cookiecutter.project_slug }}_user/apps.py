from django.apps import AppConfig


class {{ cookiecutter.project_title }}UserConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}_user"
    verbose_name = "{{ cookiecutter.project_name }} User Management"
