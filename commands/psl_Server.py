import discord
from discord.ext import commands
from discord.utils import get

class psl_Server(commands.Cog):
    def __init__(self, client, bot_name, ha_id, adm_id, mods_id, sup_id, channel_id, embed_color):
        try:
            self.client = client
            self.bot_name = bot_name
            self.embed_color = embed_color
            self.channel_id = channel_id
            self.server_name = "Polska Społeczność Linuxa"
            self.ha_id = ha_id
            self.adm_id = adm_id
            self.mods_id = mods_id
            self.sup_id = sup_id
        except Exception as e:
            print(str(e))

    @commands.command()
    async def pomoc(self, ctx):
        channel = self.client.get_channel(self.channel_id)
        embed_title = f'***Pomoc dla {self.bot_name}***'
        field1_name = f'Komendy dotyczące serwera:'
        field1_value = (
            f'**;admin** - aktualny zespół administracji i moderatorów\n'
            f'**;support** - lista wspierających serwer\n'
            f'**;sugestia <tekst sugestii>** - zgłoś sugestię dot. serwera, działa tylko na kanale #propozycje_sugestie\n'
            f'**;userinfo [użytkownik]** - sprawdź informacje o sobie (bez parametru) lub użytkowniku (z parametrem)\n'

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
        try:
            supporters = []
            channel = self.client.get_channel(self.channel_id)
            guild = get(ctx.guild.roles, id=self.sup_id)
            SupportersList = guild.members
            for user in SupportersList:
                supporters.append(user.name)
            str1 = '\n'.join(supporters)
            embed_title = f'**Wspierający serwer {self.server_name}**'
            embed_description = f'Jeśli chcesz znaleźć się na tej liście koniecznie zajrzyj na kanał **#wesprzyj_nas**'
            field1_name = f'Oto lista wspierających serwer {self.server_name}:'
            field1_value = (
                f'**{str1}**'
            )
            embedVar = discord.Embed(title=embed_title, description=embed_description, color=self.embed_color)
            embedVar.add_field(name=field1_name, value=field1_value, inline=False)
            await channel.send(embed=embedVar)
        except Exception as e:
            print(str(e))

    @commands.command()
    async def admin(self, ctx):
        try:
            head_admins = []
            admins = []
            mods = []
            channel = self.client.get_channel(self.channel_id)
            ha_guild = get(ctx.guild.roles, id=self.ha_id)
            adm_guild = get(ctx.guild.roles, id=self.adm_id)
            mods_guild = get(ctx.guild.roles, id=self.mods_id)
            for user in ha_guild.members:
                head_admins.append(user.name)
            for user in adm_guild.members:
                admins.append(user.name)
            for user in mods_guild.members:
                mods.append(user.name)
            str1 = '\n'.join(head_admins)
            str2 = '\n'.join(admins)
            str3 = '\n'.join(mods)
            embed_title = f'**Administracja serwera {self.server_name}**'
            embed_description = "Poniżej znajdziesz listę administratorów i moderatorów serwera."
            field1_name = f'Główni administratorzy:'
            field1_value = (
                f'**{str1}**'
            )
            field2_name = f'Administratorzy:'
            field2_value = (
                f'**{str2}**'
            )
            field3_name = f'Moderatorzy:'
            field3_value = (
                f'**{str3}**'
            )
            embedVar = discord.Embed(title=embed_title, description=embed_description, color=self.embed_color)
            embedVar.add_field(name=field1_name, value=field1_value, inline=False)
            embedVar.add_field(name=field2_name, value=field2_value, inline=False)
            embedVar.add_field(name=field3_name, value=field3_value, inline=False)
            await channel.send(embed=embedVar)
        except Exception as e:
            print(str(e))

    @commands.command()
    async def userinfo(self, ctx, *, user: discord.Member = None):
        channel = self.client.get_channel(self.channel_id)
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xdfa3ff, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Dołączył: ", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Zarejestrowany: ", value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Role: [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="Uprawnienia serwera: ", value=perm_string, inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        return await channel.send(embed=embed)