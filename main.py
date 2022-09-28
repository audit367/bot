from telethon import functions, types
from telethon.sync import TelegramClient
from telethon import TelegramClient, sync
from telethon import TelegramClient, events, sync


api_id = 12729769 # ваши данные, брать с my.telegram.org
api_hash = "545c1a1ec55705b8ab56d8fb408a3ad7" # ваши данные, брать с my.telegram.org


client = TelegramClient("Test", api_id, api_hash) # логинимся
client.start() # старт клиента
@client.on(events.NewMessage(chats=['maslennikovliga','dadavot'])) # список каналов, откуда будем брать посты
async def normal_handler(event):
    if isinstance(event.chat, types.Channel):
        username = event.chat.username
        rdy = "@" + str(username) # получаем юзернейм канала, откуда забрали пост
        await client.send_message("@suetolog_mestniy", rdy) # будет отправлять инфу, о том, с какого канала спизжен пост
        await client.send_message("@suetolog_mestniy", event.message) # отправка поста в канал

        await client.send_message("@wissben",rdy)  # будет отправлять инфу, о том, с какого канала спизжен пост
        await client.send_message("@wissben", event.message)  # отправка поста в канал

        # await client.send_message("@Comandante_H",rdy)  # будет отправлять инфу, о том, с какого канала спизжен пост
        # await client.send_message("@Comandante_H", event.message)  # отправка поста в канал
client.run_until_disconnected()