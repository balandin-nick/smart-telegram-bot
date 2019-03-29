import os


__all__ = [
    'PROJECT_ROOT',
    'CONFIG_FILE_PATH'
]


# --- File names:
__CONFIG_FILE_NAME = 'config.ini'

# --- Paths:
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
CONFIG_FILE_PATH = os.path.join(PROJECT_ROOT, __CONFIG_FILE_NAME)
