"""Define models for pages."""
import os

from django.conf import settings
from django.db import models
from django.template.loaders.app_directories import get_app_template_dirs
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page as WagtailPage


def get_templates_choices():
    """
    Return a list of templates as tuples usable as choices.

    Every file within a "pages" template directory that does not start
    with a dot (.) is included. Example, given the following files:
    - an_app/templates/pages/template.html
    - an_app/templates/pages/subdirectory/template.js
    - different_app/templates/pages/template.html

    The returned tuple would be:
    ```
    (
        ("pages/template.html", "pages/template.html"),
        ("pages/subdirectory/template.js", "pages/subdirectory/template.js"),
    )
    ```
    """
    template_dir_list = []
    for template_dir in get_app_template_dirs("templates"):
        if settings.BASE_DIR in template_dir:
            template_dir_list.append(template_dir)

    templates = set()
    for template_dir in template_dir_list + settings.TEMPLATES[0]["DIRS"]:
        full_path = os.path.join(template_dir, "pages")
        for base_dir, dirnames, filenames in os.walk(full_path):
            rel_dir = os.path.relpath(base_dir, template_dir)
            for filename in filenames:
                if not filename.startswith("."):
                    templates.add(os.path.join(rel_dir, filename))

    template_list = []
    for template in templates:
        template_list.append((template, template))

    return template_list


class Page(WagtailPage):
    """Define a page that uses a user selected template."""

    TEMPLATE_HELP_TEXT = _("Template to be used to render the page.")
    custom_template = models.CharField(
        max_length=255,
        blank=True,
        help_text=TEMPLATE_HELP_TEXT,
        verbose_name=_("Template"),
    )
    settings_panels = WagtailPage.settings_panels + [FieldPanel("custom_template")]

    def __init__(self, *args, **kwargs):
        """Set template based on custom_template property."""
        super().__init__(*args, **kwargs)

        self._meta.get_field("custom_template").choices = [
            ("", _("Default (%(template)s)") % {"template": self.template}),
            [_("Template override"), get_templates_choices()],
        ]

        if self.custom_template:
            self.template = self.custom_template
