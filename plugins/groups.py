from pyrogram import Client,filters

@Client.on_message(filters.command(['комманды','сommands']))
async def all_commands(client,message):
    await client.send_message(
        chat_id = message.chat.id,
        text = '/комманды\nпривет\nкак дела\nповтори ,(текст)\nчто делаешь\n/ban (никнейм)\n/unban (никнейм)\n/members'
    )

@Client.on_message(filters.command(['ban']))
async def all_commands(client,message):
    ban_user = message.text
    ban_user = ban_user.split(sep = ' ').pop(1)
    await client.ban_chat_member(message.chat.id,ban_user)

@Client.on_message(filters.command(['unban']))
async def all_commands(client,message):
    unban_user = message.text
    unban_user = unban_user.split(sep = ' ').pop(1)
    await client.unban_chat_member(message.chat.id,unban_user)

@Client.on_message(filters.command(['members']))
async def members(client,message):
    async for member in client.get_chat_members(message.chat.id):
        members = [member.user.first_name]
        members = '\n'.join(members)
        await client.send_message(
            chat_id=message.chat.id,
            text=members
        )