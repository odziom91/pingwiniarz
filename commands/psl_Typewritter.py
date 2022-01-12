import discord
from discord.ext import commands
from commands.psl_Exceptions import psl_Exception

class psl_Typewritter(commands.Cog):
    def __init__(self, client):
        try:
            self.client = client
        except Exception as e:
            print(str(e))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def tw(self, ctx, *, arg1):
        # typewritter command
        try:
            input_text = arg1
            output_text = f''
            for char in input_text:
                if char.isalpha():
                    output_text += f':regional_indicator_{char.lower()}: '
                else:
                    output_text += f':blue_square: '
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(output_text)
        except Exception as e:
            print(str(e))

    @tw.error
    async def tw_error(self, ctx):
        try:
            await ctx.channel.purge(limit=1)
            embed_title = f'**Brak uprawnień!**\n'
            embed_description = f'**Nie masz odpowiednich uprawnień do wykonania tej komendy.**\n'
            embedVar = discord.Embed(title=embed_title, description=embed_description, color=0xff0000)
            await ctx.channel.send(embed=embedVar)
        except Exception as e:
            print(str(e))