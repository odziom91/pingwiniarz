import datetime
import discord
from discord.ext import commands
from commands.psl_Exceptions import psl_Exception

class psl_Suggestions(commands.Cog):
    def __init__(self, client, suggestions_channel, embed_color):
        try:
            self.client = client
            self.embed_color = embed_color
            self.suggestions_channel = suggestions_channel
        except Exception as e:
            print(str(e))

    @commands.command()
    async def sugestia(self, ctx, *, arg1):
        # suggestion command
        try:
            get_channel_id = self.client.get_channel(ctx.channel.id)
            channel = self.client.get_channel(self.suggestions_channel)
            if get_channel_id == channel:
                await channel.purge(limit=1)
                embed = discord.Embed(title=f'Sugestia', description=f'{arg1}', color=0x3d0557, timestamp=datetime.datetime.utcnow())
                embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
                embed.set_footer(text=f'Aby dodać sugestię skorzystaj z komendy: ;sugestia <treść sugestii>')
                sugestia = await channel.send(embed=embed)
                # here you should put emoji name for "+1"
                plus = discord.utils.get(ctx.guild.emojis, name='plus1')
                await sugestia.add_reaction(plus)
                # here you should put emoji name for "-1"
                minus = discord.utils.get(ctx.guild.emojis, name='minus1')
                await sugestia.add_reaction(minus)
            else:
                embed = discord.Embed(title=f'Sugestia', description=f'Komendę należy użyć na kanale #propozycje_sugestie', color=0x3d0557, timestamp=datetime.datetime.utcnow())
                sugestia = await get_channel_id.send(embed=embed)
        except Exception as e:
            await psl_Exception(self.client, self.suggestions_channel, str(e))
