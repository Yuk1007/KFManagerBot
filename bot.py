import discord
import asyncio
from discord.ext import tasks
from datetime import datetime

TOKEN = ''
CHANNEL_ID = 0

client = discord.Client()


@client.event
async def on_ready():
    print('ログインしました')


@tasks.loop(minutes=60)
async def timer():
    now = datetime.now()
    hours = now.strftime('%H')
    if hours == '00':
        channel = client.get_channel(CHANNEL_ID)
        embed = discord.Embed(title="本日のスクリム業務", description=":grapes: スクリム申請\n"
                                                             ":apple: ロースター掲載、浮上時間の連絡\n"
                                                             ":peach: ランドマップ作成\n"
                                                             ":tangerine: 番号貼り出し、スクショ・総合結果貼り出し\n"
                                                             ":cherries: スクリム中の観戦\n"
                                                             ":ok: すべて可"
                              )
        message = await channel.send(embed=embed)
        grape = '\U0001f347'
        apple = '\U0001f34e'
        cherries = '\U0001f352'
        peach = '\U0001f351'
        tangerine = '\U0001f34a'
        ok = '\U0001f197'

        await message.add_reaction(grape)
        await message.add_reaction(apple)
        await message.add_reaction(peach)
        await message.add_reaction(tangerine)
        await message.add_reaction(cherries)

        await message.add_reaction(ok)


@timer.before_loop
async def before_timer():
    print('timer waiting...')
    await client.wait_until_ready()


timer.start()
client.run(TOKEN)
