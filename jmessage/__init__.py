from .users import *
from .common import *
from .url import *
from .groups import *
from .messages import *
from .groups import *

__version__ = '1.0.0'
VERSION = tuple(map(int,  __version__.split('.')))

# Silence urllib3 INFO logging by default

import logging
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)