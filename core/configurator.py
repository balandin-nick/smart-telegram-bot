import configparser
import os

from core.constants import CONFIG_FILE_PATH


__all__ = [
    'BotConfigurator'
]


class BotConfigurator(object):
    """ Объект-конфигуратор приложения. """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BotConfigurator, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        config_path = os.path.join(CONFIG_FILE_PATH)

        if config_path:
            self._app_config = configparser.ConfigParser()
            self._app_config.read(config_path)

        else:
            self._app_config = {
                'telegram': {
                    'token': os.environ['TELEGRAM_TOKEN'],
                    'proxy_url': os.environ.get('PROXY_URL', None)
                },
                'dialog_flow': {
                    'token': os.environ['DIALOG_FLOW_TOKEN'],
                    'lang': os.environ['DIALOG_FLOW_LANG'],
                    'session_id': os.environ['DIALOG_FLOW_SESSION_ID']
                }
            }

    @property
    def app_config(self):
        return self._app_config
