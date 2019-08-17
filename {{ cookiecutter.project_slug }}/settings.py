"""
Django settings for {{ cookiecutter.project_slug }} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import ipaddress
import os

import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "True"


# Application definition

INSTALLED_APPS = [
    # Custom apps.
    "{{ cookiecutter.project_slug }}_user.apps.{{ cookiecutter.project_title }}UserConfig",
    "pages",
    "webpack_loader",
    # WagTail apps.
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "wagtail.contrib.postgres_search",
    "modelcluster",
    "taggit",
    # Base django apps.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Development apps.
    "debug_toolbar",
    # Keep last so any app can override templates.
    "django.forms",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.core.middleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

WSGI_APPLICATION = "{{ cookiecutter.project_slug }}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {"default": None}

if "DATABASE_URL" not in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["DATABASE_NAME"],
            "USER": os.environ["DATABASE_USER"],
            "PASSWORD": os.environ["DATABASE_PASSWORD"],
            "HOST": os.environ["DATABASE_HOST"],
            "PORT": os.environ["DATABASE_PORT"],
        }
    }


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = "en-us"
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
    os.path.join(PROJECT_DIR, "styleguide", "dist"),
    os.path.join(PROJECT_DIR, "webpack", "dist"),
]
# Ensure directories exist.
# Django only creates "static". ANy other will cause an error.
for directory in STATICFILES_DIRS:
    os.makedirs(directory, exist_ok=True)


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "{{ cookiecutter.project_slug }}"
WAGTAILSEARCH_BACKENDS = {
    "default": {"BACKEND": "wagtail.contrib.postgres_search.backend"}
}


# Email
# https://docs.djangoproject.com/en/dev/topics/email/

EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)
if EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend":
    EMAIL_HOST = os.environ["EMAIL_HOST"]
    EMAIL_PORT = os.environ["EMAIL_PORT"]
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
    EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS") == "True"

if "DEFAULT_FROM_EMAIL" in os.environ:
    DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]

if "SERVER_EMAIL" in os.environ:
    SERVER_EMAIL = os.environ["SERVER_EMAIL"]

MANAGERS = [("", email.strip()) for email in os.getenv("MANAGERS", "").split()]
ADMINS = [("", email.strip()) for email in os.getenv("ADMINS", "").split()]


# Webpack-Django integration
# https://github.com/owais/django-webpack-loader

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "wp/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
    }
}


# Custom User model
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

AUTH_USER_MODEL = "{{ cookiecutter.project_slug }}_user.User"


# Authentication backends model
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#specifying-authentication-backends

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "{{ cookiecutter.project_slug }}_user.auth.SettingsBackend",
]
ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")


# https://www.fomfus.com/articles/how-to-use-ip-ranges-for-django-s-internal_ips-setting
class IpNetworks:
    """
    A Class that contains a list of IPvXNetwork objects.

    Credits to https://djangosnippets.org/snippets/1862/
    """

    networks = []

    def __init__(self, addresses):
        """Create a new IpNetwork object for each address provided."""
        for address in addresses:
            self.networks.append(ipaddress.ip_network(address))

    def __contains__(self, address):
        """Check if the given address is contained in any of our Networks."""
        for network in self.networks:
            if ipaddress.ip_address(address) in network:
                return True
        return False


if os.environ.get("INTERNAL_ADDRESSES"):
    INTERNAL_IPS = IpNetworks(os.environ["INTERNAL_ADDRESSES"].split(" "))


# SSL Settings.
# Trust Proxy header and redirect to SSL.
# https://docs.djangoproject.com/en/dev/ref/middleware/#django.middleware.security.SecurityMiddleware
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Allowed hosts
# https://docs.djangoproject.com/en/dev/topics/security/#host-headers-virtual-hosting
if os.environ.get("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(" ")


# Activate Django-Heroku.
django_heroku.settings(locals(), allowed_hosts="ALLOWED_HOSTS" not in locals())


# Add root console logger with configurable level.
LOGGING["loggers"][""] = {  # pylint: disable=undefined-variable
    "handlers": ["console"],
    "level": os.getenv("LOG_LEVEL", "WARNING"),
}
if "DB_LOG_LEVEL" in os.environ:
    LOGGING["loggers"]["django.db"] = {  # pylint: disable=undefined-variable
        "level": os.environ["DB_LOG_LEVEL"],
    }
