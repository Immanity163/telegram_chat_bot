from pyrogram import Client,filters
from random import randint

@Client.on_message(filters.regex(r'\Dривет'))
def greetings(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text="привет")

@Client.on_message(filters.regex(r'\Dак дела') )
async def how_are_you(client, message):
    await message.reply('Все в порядке,захватываю мир прямо сейчас')

@Client.on_message(filters.regex(r'\Dто делаешь') )
async def doing(client, message):
    await message.reply(f'Порабощаю людей,закончил на {randint(1,99)}%')

@Client.on_message(filters.regex(r'^\wовтори\W\W') )
async def say(client, message):
    message_editing = message.text
    message_editing = message_editing.split(',',1)
    print(message_editing)
    await message.reply(f"{''.join(message_editing[1:])}")








