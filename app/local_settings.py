import os
from django.utils.translation import ugettext_lazy as _

DEBUG = True if os.environ.get('DEBUG', 'True') else False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "+3b01&_6_m@@yb4f06$s0zno8vkybh81nbuj_q(xzk+xeih1+s"
NEVERCACHE_KEY = "l11tr%#!uc@+%$51(&+%=&z6h9yrw42(jpcj$3_&6evtu6hl%z"

# DATABASE_ROUTERS = ['eve.routers.EveRouter', 'festival.routers.FestivalRouter',]
# DATABASE_ROUTERS = ['eve.routers.EveRouter',]

DATABASES = {
    'default': {
     'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'USER': os.environ.get('DB_ENV_MYSQL_USER'),      # Not used with sqlite3.
         'PASSWORD': os.environ.get('DB_ENV_MYSQL_PASSWORD'),  # Not used with sqlite3.
         'NAME': os.environ.get('DB_ENV_MYSQL_DATABASE'),
         'HOST': 'db',      # Set to empty string for localhost. Not used with sqlite3.
         'PORT': '3306',      # Set to empty string for default. Not used with sqlite3.
    },
    'eve': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eve',
        'USER': 'eve',
        'PASSWORD': 'HmazS2frT',
        'HOST': 'pgdb',
        'PORT': '5432',
    },
    #'eve': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'eve',
    #     'USER': 'django',
    #     'PASSWORD': 'q2nqzt0WGnwWé,256',
    #     'HOST': 'eve.ircam.fr',
    #     'PORT': '5432',
    #},

}

DATABASE_ROUTERS = ['eve.routers.EveRouter',]


# EXTENSIONS AND FORMATS
# Allowed Extensions for File Upload. Lower case is important.
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.docx'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
    }

# Define different formats for allowed selections.
# This has to be a subset of EXTENSIONS.
# e.g., add ?type=image to the browse-URL ...
FILEBROWSER_SELECT_FORMATS = {
    'File': ['Folder', 'Document'],
    'Image': ['Image'],
    'Media': ['Video', 'Audio'],
    'Audio': ['Audio'],
    'Document': ['Document'],
    # for TinyMCE we can also define lower-case items
    'image': ['Image'],
    'file': ['Folder', 'Image', 'Document'],
    'media': ['Video', 'Audio'],
    'audio': ['Audio'],
}

EMAIL_HOST = 'smtp.ircam.fr'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = 'manifeste2016@ircam.fr'
EMAIL_SUBJECT_PREFIX = "IRCAM Manifeste 2016"

SITE_TITLE = 'Manifeste 2016'
SITE_TAGLINE = 'Festival 2 juin | 2 juillet 2016'

SILENCED_SYSTEM_CHECKS = ['fields.W342',]

ADMIN_MENU_ORDER = (
    (_("Content"), ("pages.Page", "blog.BlogPost", "mezzanine_agenda.Event",
        "festival.Artist", "festival.Video", "festival.Audio", "festival.Playlist",
        "festival.Featured",
        "generic.ThreadedComment", (_("Media Library"), "fb_browse"),)),
    (_("Site"), ("sites.Site", "redirects.Redirect", "conf.Setting")),
    (_("Users"), ("auth.User", "auth.Group",)),
    (_("Festival"), ("mezzanine_agenda.EventLocation",
        "mezzanine_agenda.EventCategory", "mezzanine_agenda.EventPrice",
        "festival.PageCategory",)),
)

SEARCH_MODEL_CHOICES = ()

RATINGS_ACCOUNT_REQUIRED = True

import warnings
warnings.filterwarnings(
        'ignore', r"DateTimeField .* received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

EVENT_SLUG = 'events'
EVENT_GOOGLE_MAPS_DOMAIN = 'maps.google.fr'
EVENT_PER_PAGE = 50
EVENT_USE_FEATURED_IMAGE = True
EVENT_SHOP_URL = 'http://eve.ircam.fr/manifeste.php/manifestation/'
EVENT_PASS_URL = 'http://eve.ircam.fr/manifeste.php/pass/'

TINYMCE_SETUP_JS = "/static/js/tinymce_setup.js"

SLUGIFY = 'django.template.defaultfilters.slugify'

HOME_FEATURED_ID = 1
BREAKING_NEWS_FEATURED_ID = 4

BLOG_POST_PER_PAGE = 200

FILEBROWSER_MAX_UPLOAD_SIZE = 512000000
