import discord
import asyncio
from discord.ext import tasks
from datetime import datetime

TOKEN = 'ODE4NDUzNjQ0MTUxMzU3NDQw.YEYSWg.urKdlGui_SHFYn9R-XXH3DhU8wc'
CHANNEL_ID = 788722117859737640

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
        embed = discord.Embed(title="本日のスクリム業務", description=":grapes: スクリム申請、18時の連絡\n"
                                                             ":apple: ロースター発表後のロースター掲載、観戦枠申請、浮上時間の連絡\n"
                                                             ":peach: ランドマップ作成\n"
                                                             ":tangerine: 番号貼り出し、スクショ・総合結果貼り出し\n"
                                                             ":cherries: スクリム中の観戦\n"
                                                             ":kiwi: 戦績入力\n"
                                                             ":ok: すべて可\n"
                                                             ":ng: いずれも不可\n"
                                                             ":question: 未定")
        message = await channel.send(embed=embed)
        grape = '\U0001f347'
        apple = '\U0001f34e'
        cherries = '\U0001f352'
        peach = '\U0001f351'
        tangerine = '\U0001f34a'
        kiwi = '\U0001f95d'
        ok = '\U0001f197'
        ng = '\U0001f196'
        question = '\U00002754'
        await message.add_reaction(grape)
        await message.add_reaction(apple)
        await message.add_reaction(peach)
        await message.add_reaction(tangerine)
        await message.add_reaction(cherries)
        await message.add_reaction(kiwi)
        await message.add_reaction(ok)
        await message.add_reaction(ng)
        await message.add_reaction(question)


@timer.before_loop
async def before_timer():
    print('timer waiting...')
    await client.wait_until_ready()


timer.start()
client.run(TOKEN)
