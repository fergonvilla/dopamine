from __future__ import absolute_import, unicode_literals
import os
from django.utils.translation import ugettext_lazy as _

# DJANGO SETTINGS

ADMINS = (
    ('Miguel Garcia', 'miguel.garciarod@gmail.com')
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []

SITE_ID = 1
SITE_TITLE = "DOPAMINE"
SITE_URL = "http://localhost:8000"

INTERNAL_IPS = ("127.0.0.1",)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
USE_TZ = False
USE_I18N = True
USE_L10N = True
TIME_ZONE = ('Europe/Madrid')

LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English'))
)

LANGUAGES_DICT = dict(LANGUAGES)
LANGUAGE_COOKIE_NAME = 'user_language'
DEBUG = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644

# Full filesystem path to the project.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]


# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

MEDIA_URL = STATIC_URL + "media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

ROOT_URLCONF = "urls"


TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "mezzanine.conf.context_processors.settings",
    "mezzanine.pages.context_processors.page",
)

MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",

)

MEZZANINE_APPS = (
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine.galleries",
    "mezzanine.twitter",
    # "mezzanine.accounts",
    # "mezzanine.mobile",
)

LOCAL_APPS = (
    # "myapp"
)

INSTALLED_APPS = DJANGO_APPS + MEZZANINE_APPS
INSTALLED_APPS += LOCAL_APPS

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

OPTIONAL_APPS = (
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

USE_SOUTH = True

######################
# MEZZANINE SETTINGS #
######################

# http://mezzanine.jupo.org/docs/configuration.html#default-settings
ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", "blog.BlogPost", "generic.ThreadedComment", ("Media Library", "fb_browse"),)),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),
)

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

# PAGE_MENU_TEMPLATES = (
#     (1, "Top navigation bar", "pages/menus/dropdown.html"),
#     (2, "Left-hand tree", "pages/menus/tree.html"),
#     (3, "Footer", "pages/menus/footer.html"),
# )

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         ("Image",),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         ("Another name",),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.
#
BLOG_USE_FEATURED_IMAGE = True

###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "SSH_USER": "", # SSH username for host deploying to
#     "HOSTS": ALLOWED_HOSTS[:1], # List of hosts to deploy to (eg, first host)
#     "DOMAINS": ALLOWED_HOSTS, # Domains for public site
#     "REPO_URL": "ssh://hg@bitbucket.org/user/project", # Project's repo URL
#     "VIRTUALENV_HOME":  "", # Absolute remote path for virtualenvs
#     "PROJECT_NAME": "", # Unique identifier for project
#     "REQUIREMENTS_PATH": "requirements.txt", # Project's pip requirements
#     "GUNICORN_PORT": 8000, # Port gunicorn will listen on
#     "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
#     "DB_PASS": "", # Live database password
#     "ADMIN_PASS": "", # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }

####################
# MODEL TRANSLATION #
####################


# MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', )
# # MODELTRANSLATION_AUTO_POPULATE = False
# # MODELTRANSLATION_LOADDATA_RETAIN_LOCALE = True

# MODELTRANSLATION_TRANSLATION_FILES = (
#     'cms.translation',
#     'justene.translation',
#     'blog.translation'
# )
