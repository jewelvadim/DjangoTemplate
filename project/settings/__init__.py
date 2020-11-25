try:
    from settings.prod import *
except ImportError:
    from settings.local import *

from settings.apps import *
from settings.base import *
from settings.ckeditor import *
from settings.extra import *
