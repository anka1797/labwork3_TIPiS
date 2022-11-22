# телеграм бот для отвправки форматированных сообщений
# t.me/Labwork3_bot
import telebot
token = '5809947014:AAEHwvfrIaMh2omfp-qAeOVKHUL1d06rdGU'
bot = telebot.TeleBot(token)
@bot.message_handler (commands = ['start'])

def start_message(message):
    bot.send_message(message.chat.id, '__подчёркнутый__', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '~зачёркнутый~', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '_курсив_', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '*жирный*', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '||Сейчас вас упомянут||', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '[Аня](tg://user?id=786834746) привет', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '[Написать мне:](https://t.me/anikaa_os)', parse_mode='MarkdownV2')
    bot.send_message(message.chat.id, '__подчёркнутый__, ~зачёркнутый~, _курсив_, *жирный*, ||Сейчас вас упомянут||, '
                                      '[Аня](tg://user?id=786834746) привет, [Написать мне:]('
                                      'https://t.me/anikaa_os)', parse_mode="MarkdownV2")
bot.infinity_polling()