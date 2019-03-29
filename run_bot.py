from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from core import BotConfigurator, start_command, text_message


if __name__ == '__main__':
    if BotConfigurator().app_config['telegram'].get('proxy_url'):
        request_kwargs = {'proxy_url': BotConfigurator().app_config['telegram']['proxy_url']}
        updater = Updater(
            token=BotConfigurator().app_config['telegram']['token'],
            request_kwargs=request_kwargs
        )

    else:
        updater = Updater(token=BotConfigurator().app_config['telegram']['token'])

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(MessageHandler(Filters.text, text_message))

    updater.start_polling(clean=True)
    updater.idle()
