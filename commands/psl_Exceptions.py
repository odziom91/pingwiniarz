import datetime
import discord
from discord.ext import commands, tasks

async def psl_Exception(client, ch, e):
    channel = client.get_channel(int(ch))
    dt = str(datetime.datetime.utcnow())
    title = f'O nie! Pingwiniarz spadł z rowerka!'
    description = f'''
    Data, godzina: {dt}\n
    Opis: {e}
    '''
    embedVar = discord.Embed(title=title, description=description, color=0xff0000)
    await channel.send(embed=embedVar)

