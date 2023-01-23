#Import libraries
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from like_db import LikeDB
import os

TOKEN = os.environ['TOKEN']

likedb = LikeDB('likedb.json')

#Import TOKEN from envoirment variable
# TOKEN = '5962805915:AAFQO0SG2RVhTQhbMN9FPYjDnLMC_BpfVt0'

updater = Updater(TOKEN)
#Create start command handler
def start(update:Update, context:CallbackContext):
    """Starts with picture all likes and all dislikes"""
    chat_id = update.message.chat.id
    likedb.add_user(chat_id)
    keyboar = ReplyKeyboardMarkup([
        ['Send photo']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
    

def send_photo(update:Update, context=CallbackContext):
    chat_id = update.message.chat.id
    likedb.add_user(chat_id)
    bot = context.bot
    text_likes = f'👍 {likedb.all_likes()}'
    text_dislikes = f'👎 {likedb.all_dislikes()}'
    like=InlineKeyboardButton(text=text_likes,callback_data='👍')
    dislike=InlineKeyboardButton(text=text_dislikes,callback_data='👎')
    keyboard=InlineKeyboardMarkup([
        [like,dislike]
    ])
    bot.sendPhoto(chat_id=chat_id,photo='https://avatars.mds.yandex.net/i?id=1ab9c215cc4eff5b225dacfa12a6d52b6764c3c3-5347144-images-thumbs&n=13',reply_markup=keyboard)

def quer(update:Update, context=CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    # message_id = query.message_id
    data = query.data
    bot = context.bot
    # text_likes = f'👍 {likedb.all_likes()}'
    # text_dislikes = f'👎 {likedb.all_dislikes()}'
    # like=InlineKeyboardButton(text=text_likes,callback_data='👍')
    # dislike=InlineKeyboardButton(text=text_dislikes,callback_data='👎')
    # keyboard=([
    #     [like,dislike]
    # ])
    if data == "👍":
        likedb.add_like(chat_id)
        

    elif data == "👎":
        likedb.add_dislike(chat_id)
        
    # bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=keyboard)

    query.answer('You are choosed')

#Create updater and dispatcher
updater = Updater(token=TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Send photo'), send_photo))
updater.dispatcher.add_handler(CallbackQueryHandler(quer))

#Start the bot
updater.start_polling()
updater.idle()



