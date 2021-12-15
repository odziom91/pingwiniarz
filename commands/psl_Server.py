import datetime
import discord
from discord.ext import commands, server

class psl_Server(commands.Cog):
    def __init__(self, client, bot_name, channel_id, embed_color):
        try:
            self.client = client
            self.bot_name = bot_name
            self.embed_color = embed_color
            self.channel_id = channel_id
            self.server_name = "Polska Społeczność Linuxa"
        except Exception as e:
            print(str(e))

    @commands.command()
    async def pomoc(self):
        channel = self.client.get_channel(self.channel_id)
        embed_title = f'***Pomoc dla {self.bot_name}***'
        field1_name = f'Komendy dotyczące serwera:'
        field1_value = (
            f'**;admin** - aktualny zespół administracji i moderatorów\n'
            f'**;support** - lista wspierających serwer\n'
            f'**;sugestia <tekst sugestii>** - zgłoś sugestię dot. serwera, działa tylko na kanale #propozycje_sugestie\n'

        )
        field2_name = f'Komendy dotyczące Linuksa:'
        field2_value = (
            f'**;linver** - informacja o aktualnie dostępnych wersjach wybranych dystrybucji Linuksa\n'
            f'**;kernel** - informacja o aktualnie dostępnych wersjach kernela Linuksa\n'
            f'**;gaming** - informacja o aktualnie dostępnych wersjach oprogramowania dla graczy - Lutris, Wine, Proton, etc.\n'
            f'**;pobierz** - lista hiperłączy dla wybranych dystrybucji do pobrania\n'
            f'**;nvidia** - informacja o sterownikach wideo kart graficznych NVidia'
        )
        field3_name = f'Pozostałe:'
        field3_value = (
            f'**;cat** - losuj słodkiego kota\n'
            f'**;dog** - losuj słodkiego psa\n'
            f'**;linuxmeme** - losuj mema o Linuksie\n'
            f'**;windowsmeme** - losuj mema o Windowsie\n'
            f'**;plmeme** - losuj polskiego mema\n'
            f'**;meme** - losuj zagranicznego mema\n'
            f'**;papameme** - "po maturze chodziliśmy na kremówki" ;)\n'
            f'**;unixporn** - losuj desktop\n'
            f'**;wallpaper** - inspiracja na tapetę\n'
        )
        field4_name = f'Ważne!'
        field4_value = (
            f'Więcej komend wkrótce...\n'
            f'W przypadku problemów z działaniem bota prosimy o kontakt z Administracją.\n'
        )
        embedVar = discord.Embed(title=embed_title, color=self.embed_color)
        embedVar.add_field(name=field1_name, value=field1_value, inline=False)
        embedVar.add_field(name=field2_name, value=field2_value, inline=False)
        embedVar.add_field(name=field3_name, value=field3_value, inline=False)
        embedVar.add_field(name=field4_name, value=field4_value, inline=False)
        await channel.send(embed=embedVar)

    @commands.command()
    async def support(self, ctx):
        channel = self.client.get_channel(self.channel_id)
        supporters = []
        for user in ctx.guild.members:
            if "Wspierający" in user.roles:
                supporters.append(user)
                print("Znalazłem wspierającego")
        str1 = '\n'.join(supporters)
        embed_title = f'**Wspierający serwer {self.server_name}**'
        embed_description = f'Jeśli chcesz znaleźć się na tej liście koniecznie zajrzyj na kanał **#wesprzyj_nas**'
        field1_name = f'**Oto lista wspierających serwer {self.server_name}:**'
        field1_value = (
            f'{str1}'
        )
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=self.embed_color)
        embedVar.add_field(name=field1_name, value=field1_value, inline=False)
        await channel.send(embed=embedVar)