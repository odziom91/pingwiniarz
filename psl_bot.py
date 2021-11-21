import configparser
import discord
import time
from random import randint
from modules.psl_GetVideo import *
from modules.psl_GetVersion import *
from modules.psl_Fun import *
from discord.ext import commands, tasks

##### init vars
config = configparser.ConfigParser()
config.read('./psl_config.ini')
bot_name = config.get("config","bot_name")
server_name = config.get("config","server_name")
cfg_channel = int(config.get("config","channel_id"))
godfather = config.get("config","godfather").split(",")
head_admins = config.get("config","head_admins").split(",")
admins = config.get("config","admins").split(",")
mods = config.get("config","mods").split(",")
supporters = config.get("config","supporters").split(",")
token = config.get("config","token")
embed_color = 0xeace37
#####

##### discord part
activity = discord.Game(name=f';pomoc | {server_name}')
client = commands.Bot(command_prefix=";", activity=activity, status=discord.Status.idle)
client.remove_command("help")

## events
@client.event
async def on_ready():
    print("Bot uruchomiony.")
    chg_presence.start()
    gaming_version_checker.start()
    os_version_checker.start()
    nvidia_version_checker.start()

@client.event
async def on_command_error(ctx, error):
    channel = client.get_channel(cfg_channel)
    embed_title = f'Błąd'
    field1_name = f'Wystąpił błąd podczas wykonywania komendy.'
    field1_value = (
        f'Jeśli problem będzie się powtarzał prosimy o kontakt z Administracją.'
    )
    embedVar = discord.Embed(title=embed_title, color=0xff0000)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    await channel.send(embed=embedVar)

## commands
@client.command()
async def pomoc(ctx):
    channel = client.get_channel(cfg_channel)
    embed_title = f'***Pomoc dla {bot_name}***'
    field1_name = f'Komendy dotyczące serwera:'
    field1_value = (
        f'**;admin** - aktualny zespół administracji i moderatorów\n'
        f'**;support** - lista wspierających serwer'
    )
    field2_name = f'Komendy dotyczące Linuksa:'
    field2_value = (
        f'**;linver** - informacja o aktualnie dostępnych wersjach wybranych dystrybucji Linuksa\n'
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
        f'**;papameme** - "po maturze chodziliśmy na kremówki" ;)'
        f'**;unixporn** - losuj desktop\n'
        f'**;wallpaper** - inspiracja na tapetę\n'
    )
    field4_value = (
        f'Więcej komend wkrótce...\n'
        f'W przypadku problemów z działaniem bota prosimy o kontakt z Administracją.\n'
    )
    field4_name = f'Ważne!'
    field4_value = (
        f'Więcej komend wkrótce...\n'
        f'W przypadku problemów z działaniem bota prosimy o kontakt z Administracją.\n'
    )
    embedVar = discord.Embed(title=embed_title, color=0x00ff00)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    embedVar.add_field(name=field2_name, value=field2_value, inline=False)
    embedVar.add_field(name=field3_name, value=field3_value, inline=False)
    embedVar.add_field(name=field4_name, value=field4_value, inline=False)
    await channel.send(embed=embedVar)
    

@client.command()
async def nvidia(ctx):
    config = configparser.ConfigParser()
    config.read('./psl_version_checker.ini')
    cfg_nv_nfb = config.get("video", "nvidia_nfb")
    cfg_nv_pb = config.get("video", "nvidia_pb")

    channel = client.get_channel(cfg_channel)
    embed_title = f'Aktualne sterowniki do kart graficznych NVidia'
    field1_name = f'NVidia - New Feature Branch'
    field1_value = (
        f'Wersja: **{cfg_nv_nfb}**'
    )
    field2_name = f'NVidia - Production Branch'
    field2_value = (
        f'Wersja: **{cfg_nv_pb}**'
    )
    field3_name = f'Porada'
    field3_value = (
        f'Jeśli to możliwe zalecamy instalację sterownika z linii New Feature Branch.'
    )
    embedVar = discord.Embed(title=embed_title, color=0x00ff00)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    embedVar.add_field(name=field2_name, value=field2_value, inline=False)
    embedVar.add_field(name=field3_name, value=field3_value, inline=False)
    await channel.send(embed=embedVar)


@client.command()
async def gaming(ctx):
    channel = client.get_channel(cfg_channel)

    wait_title = f'Proszę poczekać - pobieram aktualne dane...'
    wait_embed = discord.Embed(title=wait_title, color=0x00ff00)
    await channel.send(embed=wait_embed)

    wine_versions = GetVersion_Wine()
    lutris_version = GetVersion_Lutris()
    proton_version = GetVersion_Proton()
    proton_ge_version = GetVersion_Proton_GE()
    wine_ge_version = GetVersion_Wine_GE()
    wine_kronfourek_version = GetVersion_Wine_Kronfourek()

    embed_title = f'**Aktualne wersje oprogramowania dla graczy**'
    field1_name = f'**Lutris**'
    field1_value = (
        f'Wersja: **{lutris_version}**'
    )
    field2_name = f'Wine'
    field2_value = (
        f'Stable - wersja: **{wine_versions[0]}**\n'
        f'Testing - wersja: **{wine_versions[1]}**'
    )
    field3_name = f'Proton'
    field3_value = (
        f'Wersja: **{proton_version}**'
    )
    field4_name = f'Proton-GE'
    field4_value = (
        f'Wersja: **{proton_ge_version}**'
    )
    field5_name = f'Wine-GE'
    field5_value = (
        f'Wersja: **{wine_ge_version}**'
    )
    field6_name = f'Kron4ek Wine'
    field6_value = (
        f'Wersja: **{wine_kronfourek_version}**'
    )
    embedVar = discord.Embed(title=embed_title, color=0x00ff00)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    embedVar.add_field(name=field2_name, value=field2_value, inline=False)
    embedVar.add_field(name=field3_name, value=field3_value, inline=False)
    embedVar.add_field(name=field4_name, value=field4_value, inline=False)
    embedVar.add_field(name=field5_name, value=field5_value, inline=False)
    embedVar.add_field(name=field6_name, value=field6_value, inline=False)
    await channel.send(embed=embedVar)


@client.command()
async def linver(ctx):
    channel = client.get_channel(cfg_channel)
    distrowatch_beginners = []
    distrowatch_middle = []
    distrowatch_advanced = []
    os_list_beginners = [
        ("ubuntu", 1, "Ubuntu"),
        ("mint", 0, "Linux Mint"),
        ("elementary", 0, "Elementary OS"),
        ("zorin", 0, "Zorin OS"),
        ("solus", 0, "Solus"),
        ("popos", 0, "Pop!_OS")
    ]
    os_list_middle = [
        ("fedora", 1, "Fedora"),
        ("opensuse", 1, "openSUSE"),
        ("endeavour", 0, "EndeavourOS"),
        ("mx", 0, "MX Linux"),
        ("manjaro", 1, "Manjaro Linux"),
        ("garuda", 0, "Garuda Linux")
    ]
    os_list_advanced = [
        ("arch", 0, "Arch Linux"),
        ("gentoo", 1, "Gentoo Linux"),
        ("slackware", 0, "Slackware Linux"),
        ("lfs", 1, "Linux From Scratch"),
        ("qubes", 0, "Qubes OS"),
        ("nixos", 0, "NixOS")
    ]
    for os in os_list_beginners:
        os_1, os_2, os_3 = os
        chk_os = GetVersion_Distrowatch_OS(os_1, os_2)
        distrowatch_beginners.append(f'{os_3}: **{chk_os}**')
    for os in os_list_middle:
        os_1, os_2, os_3 = os
        chk_os = GetVersion_Distrowatch_OS(os_1, os_2)
        distrowatch_middle.append(f'{os_3}: **{chk_os}**')
    for os in os_list_advanced:
        os_1, os_2, os_3 = os
        chk_os = GetVersion_Distrowatch_OS(os_1, os_2)
        distrowatch_advanced.append(f'{os_3}: **{chk_os}**')
    str1 = '\n'.join(distrowatch_beginners)
    str2 = '\n'.join(distrowatch_middle)
    str3 = '\n'.join(distrowatch_advanced)
    embed_title = f'**Aktualne wersje najpopularniejszych dystrybucji Linuksa**'
    field1_name = f'**Dla początkujących użytkowników:**'
    field1_value = (
        f'{str1}'
    )
    field2_name = f'**Dla średnio zaawansowanych użytkowników:**'
    field2_value = (
        f'{str2}'
    )
    field3_name = f'**Dla zaawansowanych użytkowników:**'
    field3_value = (
        f'{str3}'
    )
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    embedVar.add_field(name=field2_name, value=field2_value, inline=False)
    embedVar.add_field(name=field3_name, value=field3_value, inline=False)
    await channel.send(embed=embedVar)

@client.command()
async def pobierz(ctx):
    channel = client.get_channel(cfg_channel)
    embed_title = f'**Pobierz Linuksa!**'
    embed_description = "Wybierz jedną z dystrybucji poniżej. Dystrybucje podzielone są według stopnia zaawansowania."
    field1_name = f'**Dla początkujących użytkowników:**'
    field1_value = (
        f'**Ubuntu** - pobierz: https://www.ubuntu.com/download/ \n'
        f'**Linux Mint** - pobierz: https://www.linuxmint.com/download.php \n'
        f'**Elementary OS** - pobierz: https://elementary.io/ \n'
        f'**Zorin OS** - pobierz: https://zorinos.com/download \n'
        f'**Solus** - pobierz: https://getsol.us/download/ \n'
        f'**Pop!_OS** - pobierz: https://pop.system76.com/ \n'
    )
    field2_name = f'**Dla średnio-zaawansowanych użytkowników:**'
    field2_value = (
        f'**Fedora** - pobierz: https://getfedora.org/pl/ \n'
        f'**openSUSE** - pobierz: https://get.opensuse.org/pl/ \n'
        f'**Manjaro** - pobierz: https://manjaro.org/download/ \n'
        f'**EndeavourOS** - pobierz: https://endeavouros.com/latest-release/ \n'
        f'**MX Linux** - pobierz: https://mxlinux.org/download-links/#Mirrors \n'
        f'**Garuda Linux** - pobierz: https://garudalinux.org/downloads.html \n'
    )
    field3_name = f'**Dla zaawansowanych użytkowników:**'
    field3_value = (
        f'**Arch Linux** - pobierz: https://archlinux.org/download/ \n'
        f'**Gentoo Linux** - pobierz: http://www.gentoo.org/main/en/mirrors.xml \n'
        f'**Slackware Linux** - pobierz: http://www.slackware.com/getslack/ \n'
        f'**Linux From Scratch** - pobierz: http://www.linuxfromscratch.org/lfs/download.html \n'
        f'**Qubes OS** - pobierz: https://www.qubes-os.org/downloads/ \n'
        f'**NixOS** - pobierz: http://nixos.org/nixos/download.html \n'
    )
    embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    embedVar.add_field(name=field2_name, value=field2_value, inline=False)
    embedVar.add_field(name=field3_name, value=field3_value, inline=False)
    await channel.send(embed=embedVar)


@client.command()
async def admin(ctx):
    channel = client.get_channel(cfg_channel)
    str1 = '\n'.join(head_admins)
    str2 = '\n'.join(admins)
    str3 = '\n'.join(mods)
    embed_title = f'**Administracja serwera {server_name}**'
    embed_description = "Poniżej znajdziesz listę administratorów i moderatorów serwera."
    field1_name = f'**Główni administratorzy:**'
    field1_value = (
        f'{str1}'
    )
    field2_name = f'**Administratorzy:**'
    field2_value = (
        f'{str2}'
    )
    field3_name = f'**Moderatorzy:**'
    field3_value = (
        f'{str3}'
    )
    embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    embedVar.add_field(name=field2_name, value=field2_value, inline=False)
    embedVar.add_field(name=field3_name, value=field3_value, inline=False)
    await channel.send(embed=embedVar)


@client.command()
async def support(ctx):
    channel = client.get_channel(cfg_channel)
    str1 = '\n'.join(supporters)
    embed_title = f'**Wspierający serwer {server_name}**'
    embed_description = f'Jeśli chcesz znaleźć się na tej liście koniecznie zajrzyj na kanał **#wesprzyj_nas**'
    field1_name = f'**Oto lista wspierających serwer {server_name}:**'
    field1_value = (
        f'{str1}'
    )
    embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
    embedVar.add_field(name=field1_name, value=field1_value, inline=False)
    await channel.send(embed=embedVar)

@client.command()
async def cat(ctx):
    channel = client.get_channel(cfg_channel)
    cat = GetCat()
    embed_title = f'**Wylosowano kociaka**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=cat)
    await channel.send(embed=embedVar)

@client.command()
async def dog(ctx):
    channel = client.get_channel(cfg_channel)
    dog = GetReddit('dogpictures')
    embed_title = f'**Wylosowano psiaka**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=dog)
    await channel.send(embed=embedVar)

@client.command()
async def linuxmeme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('linuxmemes')
    embed_title = f'**Memy o Linuksie**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=meme)
    await channel.send(embed=embedVar)

@client.command()
async def windowsmeme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('windowsmemes')
    embed_title = f'**Memy o Windowsie**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=meme)
    await channel.send(embed=embedVar)

@client.command()
async def plmeme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('Polska_wpz')
    embed_title = f'**Polskie memy z Reddita**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=meme)
    await channel.send(embed=embedVar)

@client.command()
async def meme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('memes')
    embed_title = f'**Memy z Reddita**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=meme)
    await channel.send(embed=embedVar)

@client.command()
async def papameme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetPapiez()
    channel = client.get_channel(cfg_channel)
    embed_title = f'**Papa Meme from API by Mopsior**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=meme)
    await channel.send(embed=embedVar)

@client.command()
async def unixporn(ctx):
    channel = client.get_channel(cfg_channel)
    unixporn = GetReddit('unixporn')
    embed_title = f'**r/unixporn**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=unixporn)
    await channel.send(embed=embedVar)

@client.command()
async def wallpaper(ctx):
    channel = client.get_channel(cfg_channel)
    wp = GetWallpaper()
    embed_title = f'**Wylosowano tapetkę**'
    embedVar = discord.Embed(title=embed_title, color=embed_color)
    embedVar.set_image(url=wp)
    await channel.send(embed=embedVar)


## tasks
@tasks.loop(seconds=25.0)
async def chg_presence():
    komunikaty = [
        ";pomoc | napisz do mnie ;)",
        ";pomoc | pomoc",
        ";admin | administracja",
        ";pobierz | pobierz Linuksa!"
    ]
    await client.change_presence(activity=discord.Game(name=komunikaty[randint(0, 2)]))

@tasks.loop(minutes=15)
async def os_version_checker():
    channel = client.get_channel(cfg_channel)
    config = configparser.ConfigParser()
    config.read('./psl_version_checker.ini')
    os_list = [
        ("ubuntu", 1, "Ubuntu"),
        ("popos", 0, "Pop!_OS"),
        ("elementary", 0, "Elementary OS"),
        ("mint", 0, "Linux Mint"),
        ("zorin", 0, "Zorin OS"),
        ("solus", 0, "Solus"),
        ("garuda", 0, "Garuda Linux"), 
        ("endeavour", 0, "EndeavourOS"),
        ("manjaro", 1, "Manjaro Linux"),
        ("mx", 0, "MX Linux"),
        ("fedora", 1, "Fedora"),
        ("opensuse", 1, "openSUSE"),
        ("arch", 0, "Arch Linux"),
        ("gentoo", 1, "Gentoo Linux"),
        ("slackware", 0, "Slackware Linux"),
        ("lfs", 1, "Linux From Scratch"),
        ("qubes", 0, "Qubes OS"),
        ("nixos", 0, "NixOS")
    ]
    for os in os_list:
        os_1, os_2, os_3 = os
        cfg_os = config.get("os", os_1)
        chk_os = GetVersion_Distrowatch_OS(os_1, os_2)
        if chk_os != cfg_os:
            embed_title = f'**Hej,** nowa wersja systemu operacyjnego **{os_3}** została wydana!'
            embed_description = f'Aktualna wersja to: **{chk_os}**\nZachęcamy do aktualizacji systemu!'
            embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
            await channel.send(embed=embedVar)
            config.set("os", os_1, chk_os)
    with open('./psl_version_checker.ini', 'w') as configfile:
        config.write(configfile)

@tasks.loop(minutes=15)
async def gaming_version_checker():
    channel = client.get_channel(cfg_channel)
    config = configparser.ConfigParser()
    config.read('./psl_version_checker.ini')
    cfg_wine = config.get("gaming", "wine")
    cfg_wine_testing = config.get("gaming", "wine_testing")
    cfg_proton = config.get("gaming", "proton")
    cfg_proton_ge = config.get("gaming", "proton_ge")
    cfg_wine_ge = config.get("gaming", "wine_ge")
    cfg_wine_kronfourek = config.get("gaming", "wine_kronfourek")
    cfg_lutris = config.get("gaming", "lutris")
    chk_wine, chk_wine_testing = GetVersion_Wine()
    chk_proton = GetVersion_Proton()
    chk_proton_ge = GetVersion_Proton_GE()
    chk_wine_ge = GetVersion_Wine_GE()
    chk_wine_kronfourek = GetVersion_Wine_Kronfourek().strip()
    chk_lutris = GetVersion_Lutris()
    if chk_wine != cfg_wine:
        embed_title = f'**Hej,** pojawiła się nowa wersja Wine Stable!'
        embed_description = f'Aktualna wersja to: **{chk_wine}!**\nZachęcamy do aktualizacji!'
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
        await channel.send(embed=embedVar)
        config.set("gaming", "wine", chk_wine)
    if chk_wine_testing != cfg_wine_testing:
        embed_title = f'**Hej,** pojawiła się nowa wersja Wine Testing!'
        embed_description = f'Aktualna wersja to: **{chk_wine_testing}!**\nZachęcamy do aktualizacji!'
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
        await channel.send(embed=embedVar)
        config.set("gaming", "wine_testing", chk_wine_testing)
    if chk_proton != cfg_proton:
        embed_title = f'**Hej,** pojawiła się nowa wersja Proton!'
        embed_description = f'Aktualna wersja to: **{chk_proton}!**\nZachęcamy do aktualizacji!'
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
        await channel.send(embed=embedVar)
        config.set("gaming", "proton", chk_proton)
    if chk_proton_ge != cfg_proton_ge:
        embed_title = f'**Hej,** pojawiła się nowa wersja Proton-GE (GloriousEggroll)!'
        embed_description = f'Aktualna wersja to: **{chk_proton_ge}!**\nZachęcamy do aktualizacji!'
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
        await channel.send(embed=embedVar)
        config.set("gaming", "proton_ge", chk_proton_ge)
    if chk_wine_ge != cfg_wine_ge:
        embed_title = f'**Hej,** pojawiła się nowa wersja Wine-GE (GloriousEggroll)!'
        embed_description = f'Aktualna wersja to: **{chk_wine_ge}!**\nZachęcamy do aktualizacji!'
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
        await channel.send(embed=embedVar)
        config.set("gaming", "wine_ge", chk_wine_ge)
    if chk_wine_kronfourek != cfg_wine_kronfourek:
        embed_title = f'**Hej,** pojawiła się nowa wersja Wine Kron4ek (Vanilla build)!'
        embed_description = f'Aktualna wersja to: **{chk_wine_kronfourek}!**\nZachęcamy do aktualizacji!'
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
        await channel.send(embed=embedVar)
        config.set("gaming", "wine_kronfourek", chk_wine_kronfourek)
    if chk_lutris != cfg_lutris:
        embed_title = f'**Hej,** pojawiła się nowa wersja Lutris!'
        embed_description = f'Aktualna wersja to: **{chk_lutris}!**\nZachęcamy do aktualizacji!'
        embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
        await channel.send(embed=embedVar)
        config.set("gaming", "lutris", chk_lutris)
    with open('./psl_version_checker.ini', 'w') as configfile:
        config.write(configfile)

@tasks.loop(hours=1)
async def nvidia_version_checker():
    channel = client.get_channel(cfg_channel)
    config = configparser.ConfigParser()
    config.read('./psl_version_checker.ini')
    cfg_nv_nfb = config.get("video", "nvidia_nfb")
    cfg_nv_pb = config.get("video", "nvidia_pb")
    chk_nv_nfb_name, chk_nv_nfb_version, chk_nv_nfb_date = GetNvidia_nfb()
    chk_nv_pb_name, chk_nv_pb_version, chk_nv_pb_date = GetNvidia_pb()
    if chk_nv_nfb_version != cfg_nv_nfb:
            embed_title = f'**Hej,** została wydana nowa wersja sterownika NVidia - "New Features Branch".'
            embed_description = f'Nazwa sterownika: {chk_nv_nfb_name}\nWersja: **{chk_nv_nfb_version}**\nData wydania: **{chk_nv_nfb_date}**'
            embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
            await channel.send(embed=embedVar)
            config.set("video", "nvidia_nfb", chk_nv_nfb_version)
    if chk_nv_pb_version != cfg_nv_pb:
            await channel.send(
                f'Hej, użytkownicy kart graficznych NVidia!\nZostała wydana nowa wersja sterownika "Production Branch".\nNazwa sterownika: {chk_nv_pb_name}\nWersja: **{chk_nv_pb_version}**\nData wydania: **{chk_nv_pb_date}**\n'
            )
            embed_title = f'**Hej,** została wydana nowa wersja sterownika NVidia - "Production Branch".'
            embed_description = f'Nazwa sterownika: {chk_nv_pb_name}\nWersja: **{chk_nv_pb_version}**\nData wydania: **{chk_nv_pb_date}**'
            embedVar = discord.Embed(title=embed_title, description=embed_description, color=embed_color)
            await channel.send(embed=embedVar)
            config.set("video", "nvidia_pb", chk_nv_pb_version)
    with open('./psl_version_checker.ini', 'w') as configfile:
        config.write(configfile)


## init
if __name__ == '__main__':
    client.run(token)
