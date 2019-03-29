import json
import apiai

from core.configurator import BotConfigurator


__all__ = [
    'start_command',
    'text_message'
]


def start_command(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Привет, давай пообщаемся?'
    )


def text_message(bot, update):
    configs = BotConfigurator().app_config

    # Настройки DialogFlow:
    request = apiai.ApiAI(client_access_token=configs['dialog_flow']['token']).text_request()

    request.lang = configs['dialog_flow']['lang']
    request.session_id = configs['dialog_flow']['session_id']
    request.query = update.message.text

    # Получение и отправка ответа:
    response_json = json.loads(request.getresponse().read().decode('utf-8'))
    response = response_json['result']['fulfillment']['speech']

    bot.send_message(
        chat_id=update.message.chat_id,
        text=response and response or 'Я Вас не совсем понял!'
    )
