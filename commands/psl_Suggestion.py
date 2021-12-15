import datetime
import discord
from discord.ext import commands, tasks

class psl_Suggestions(commands.Cog):
    def __init__(self, client, suggestions_channel, embed_color):
        self.client = client
        self.embed_color = embed_color
        self.suggestions_channel = suggestions_channel

    @commands.command()
    async def sugestia(self, ctx, *, arg1):
        channel = self.client.get_channel(self.suggestions_channel)
        await channel.send(f'{arg1}')
        await channel.purge(limit=1)
        embed = discord.Embed(title=f'Sugestia', description=f'{arg1}', color=0x3d0557, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        embed.set_footer(text=f'\u200b ;zasugeruj <treść sugestii>')
        sugestia = await channel.send(embed=embed)
        plus = discord.utils.get(ctx.guild.emojis, name='1_')
        await sugestia.add_reaction(plus)
        minus = discord.utils.get(ctx.guild.emojis, name='1_~1')
        await sugestia.add_reaction(minus)