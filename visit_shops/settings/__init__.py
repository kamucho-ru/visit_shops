from django.utils.module_loading import import_string

import os


current_settings = os.environ.get("DJANGO_SETTINGS_MODULE")

try:
    import_string(current_settings)
except ImportError:
    from .default import *  # noqa

print("loaded settings " + current_settings + "\n")
