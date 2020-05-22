from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import googletrans
from googletrans import Translator
Lang_list = googletrans.LANGUAGES
trns = Translator()
TOKEN='1006250609:AAGq-RTizj2zcPuGkpGsakpTqv5Gj1I4HoY'
global dest_lang
dest_lang = {}


updater = Updater(TOKEN)    #connection
dp = updater.dispatcher     #way to transmit handlers

def start_handler(bot,update):
    print(update)
    bot.send_message(update['message']['chat']['id'], 'Hello!\nEnter your sentence here to be translated.\n(from any language you like into English /en or Persian /fa)\nJust select one of them')
    status = open("status.txt", "a+")
    status.writelines(str(update))
    status.close()

def en_detect(bot, update):
    global dest_lang
    dest_lang[update['message']['chat']['id']] = 'en'
    bot.send_message(update['message']['chat']['id'], "English selected. Now send me your text.")
def fa_detect(bot, update):
    global dest_lang
    dest_lang[update['message']['chat']['id']] = 'fa'
    bot.send_message(update['message']['chat']['id'], "Persian selected. Now send me your text.")

def anythg(bot, update):
    print("mshhnldrssss is:\n\n" + str(update))
    print(f"\n{dest_lang[update['message']['chat']['id']]}")
    org = update['message']['text']
    print("\nhere 2")
    res = trns.translate(org, dest=dest_lang[update['message']['chat']['id']])
    src_lang = Lang_list[res.src]
    txt = res.text
    bot.send_message(update['message']['chat']['id'], f"Source language is \"{src_lang}\"\nTranslation to {Lang_list[dest_lang]} : {txt}")
    bot.forward_message(144573031, update['message']['chat']['id'], update['message']['message_id'])
    bot.send_message(144573031, "\n@"+update['message']['chat']['username'])

h = CommandHandler('start', start_handler)  #associating command and function
dp.add_handler(h) #giving handler (h) to dispatcher

en = CommandHandler('en', en_detect)
dp.add_handler(en)

fa = CommandHandler('fa', fa_detect)
dp.add_handler(fa)

g = MessageHandler(Filters.text, anythg)
dp.add_handler(g)

updater.start_polling()
updater.idle()


# from now < may 22th > added to git
#dddddddddd
