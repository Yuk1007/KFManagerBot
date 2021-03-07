import discord
import asyncio
from discord.ext import tasks
from datetime import datetime

TOKEN = 'ODE2OTY4OTM5MTI4MDk0Nzcw.YECrnQ.AcK1cZvQMq_AFmTxpUQA4YgMf18'
CHANNEL_ID = 767073166563606578

client = discord.Client()


@client.event
async def on_ready():
    print('ログインしました')


@tasks.loop(seconds=10)
async def timer():
    now = datetime.now()
    hours = now.strftime('%H:%M')
    if hours == '11:54':
        channel = client.get_channel(CHANNEL_ID)
        message = await channel.send('スクリムに出る人は○出ない人は×を押してね！')
        circle = '\U00002b55'
        batu = '\U0000274c'
        await message.add_reaction(circle)
        await message.add_reaction(batu)

@timer.before_loop
async def before_timer():
    print('timer waiting...')
    await client.wait_until_ready()


timer.start()
client.run(TOKEN)