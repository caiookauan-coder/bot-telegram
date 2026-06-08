  telebot
    os

TOKEN = os.getenv("8037756153:AAHC3HRsY1TEDtWW9ZtGRKETkbCYv79Yr1A"
                 )

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambdam: True)
defresponder(message):
    bot.reply_to(message, "Olá! Estou funcionando.")

bot.infinity_polling()
