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
    await channel.send(
        f'Nieprawidłowa komenda. Lista komend dostępna jest po wpisaniu `;pomoc`.'
    )

## commands
@client.command()
async def pomoc(ctx):
    channel = client.get_channel(cfg_channel)
    await channel.send(
        f'***Pomoc dla {bot_name}***\n'
        f'\n'
        f'Komendy dotyczące serwera:\n'
        f'**;admin** - aktualny zespół administracji i moderatorów\n'
        f'**;support** - lista wspierających serwer'
        f'\n'
        f'Komendy dotyczące Linuksa:\n'
        f'**;linver** - informacja o aktualnie dostępnych wersjach wybranych dystrybucji Linuksa\n'
        f'**;gaming** - informacja o aktualnie dostępnych wersjach oprogramowania dla graczy - Lutris, Wine, Proton, etc.\n'
        f'**;pobierz** - lista hiperłączy dla wybranych dystrybucji do pobrania\n'
        f'**;nvidia** - informacja o sterownikach wideo kart graficznych NVidia'
        f'\n'
        f'Pozostałe:\n'
        f'**;cat** - losuj słodkiego kota\n'
        f'**;dog** - losuj słodkiego psa\n'
        f'**;linuxmeme** - losuj mema o Linuksie\n'
        f'**;windowsmeme** - losuj mema o Windowsie\n'
        f'**;plmeme** - losuj polskiego mema\n'
        f'**;meme** - losuj zagranicznego mema\n'
        f'**;unixporn** - losuj desktop\n'
        f'**;wallpaper** - inspiracja na tapetę\n'
        f'\n'
        f'Więcej komend wkrótce...\n'
        f'W przypadku problemów z działaniem bota prosimy o kontakt z Administracją.\n'
    )

@client.command()
async def nvidia(ctx):
    channel = client.get_channel(cfg_channel)
    config = configparser.ConfigParser()
    config.read('./psl_version_checker.ini')
    cfg_nv_nfb = config.get("video", "nvidia_nfb")
    cfg_nv_pb = config.get("video", "nvidia_pb")
    await channel.send(
                f'***Oto najnowsze wersje sterowników wideo dla kart graficznych NVidia***\n'
                f'NVidia - New Feature Branch: **{cfg_nv_nfb}**\n'
                f'NVidia - Production Branch: **{cfg_nv_pb}**\n'
                f'\n'
                f'Jeśli to możliwe zalecamy instalację sterownika z linii New Feature Branch.\n'
            )

@client.command()
async def gaming(ctx):
    channel = client.get_channel(cfg_channel)
    await channel.send(
        f'Proszę poczekać - pobieram aktualne dane...\n\n'
    )
    wine_versions = GetVersion_Wine()
    lutris_version = GetVersion_Lutris()
    proton_version = GetVersion_Proton()
    proton_ge_version = GetVersion_Proton_GE()
    wine_ge_version = GetVersion_Wine_GE()
    wine_kronfourek_version = GetVersion_Wine_Kronfourek()
    await channel.send(
        f'***Aktualne wersje oprogramowania dla graczy***\n'
        f'**Lutris**\nStable: {lutris_version}\n'
        f'***Oficjalne wersje Wine/Proton***\n'
        f'**Wine**\nStable: {wine_versions[0]}\nTesting: {wine_versions[1]}\n'
        f'**Proton**\nStable: {proton_version}\n'
        f'***Nieoficjalne wersje Wine/Proton***\n'
        f'**Proton-GE**\nStable: {proton_ge_version}\n'
        f'**Wine-GE**\nStable: {wine_ge_version}\n'
        f'**Kron4ek Wine**\nStable: {wine_kronfourek_version}\n'
    )

@client.command()
async def linver(ctx):
    channel = client.get_channel(cfg_channel)
    distrowatch = []
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
    distrowatch.append(f'***Aktualne wersje najpopularniejszych dystrybucji Linuksa***')
    distrowatch.append(f'**Dla początkujących użytkowników:**')
    for os in os_list_beginners:
        os_1, os_2, os_3 = os
        chk_os = GetVersion_Distrowatch_OS(os_1, os_2)
        distrowatch.append(f'{os_3}: **{chk_os}**')
    distrowatch.append(f'**Dla średnio zaawansowanych użytkowników:**')
    for os in os_list_middle:
        os_1, os_2, os_3 = os
        chk_os = GetVersion_Distrowatch_OS(os_1, os_2)
        distrowatch.append(f'{os_3}: **{chk_os}**')
    distrowatch.append(f'**Dla zaawansowanych użytkowników:**')
    for os in os_list_advanced:
        os_1, os_2, os_3 = os
        chk_os = GetVersion_Distrowatch_OS(os_1, os_2)
        distrowatch.append(f'{os_3}: **{chk_os}**')
    str1 = '\n'.join(distrowatch)
    await channel.send(
        f'{str1}'
    )

@client.command()
async def pobierz(ctx):
    channel = client.get_channel(cfg_channel)
    await channel.send(
        f'***Hiperłącza do pobrania najpopularniejszych dystrybucji Linux***'
    )
    await channel.send(
        f'**Dla początkujących użytkowników:**\n'
        f'**Ubuntu** - pobierz: https://www.ubuntu.com/download/ \n'
        f'**Linux Mint** - pobierz: https://www.linuxmint.com/download.php \n'
        f'**Elementary OS** - pobierz: https://elementary.io/ \n'
        f'**Zorin OS** - pobierz: https://zorinos.com/download \n'
        f'**Solus** - pobierz: https://getsol.us/download/ \n'
        f'**Pop!_OS** - pobierz: https://pop.system76.com/ \n'
    )
    time.sleep(3)
    await channel.send(
        f'**Dla średnio-zaawansowanych użytkowników:**\n'
        f'**Fedora** - pobierz: https://getfedora.org/pl/ \n'
        f'**openSUSE** - pobierz: https://get.opensuse.org/pl/ \n'
        f'**Manjaro** - pobierz: https://manjaro.org/download/ \n'
        f'**EndeavourOS** - pobierz: https://endeavouros.com/latest-release/ \n'
        f'**MX Linux** - pobierz: https://mxlinux.org/download-links/#Mirrors \n'
        f'**Garuda Linux** - pobierz: https://garudalinux.org/downloads.html \n'
    )
    time.sleep(3)
    await channel.send(
        f'**Dla zaawansowanych użytkowników:**\n'
        f'**Arch Linux** - pobierz: https://archlinux.org/download/ \n'
        f'**Gentoo Linux** - pobierz: http://www.gentoo.org/main/en/mirrors.xml \n'
        f'**Slackware Linux** - pobierz: http://www.slackware.com/getslack/ \n'
        f'**Linux From Scratch** - pobierz: http://www.linuxfromscratch.org/lfs/download.html \n'
        f'**Qubes OS** - pobierz: https://www.qubes-os.org/downloads/ \n'
        f'**NixOS** - pobierz: http://nixos.org/nixos/download.html \n'
    )
    time.sleep(3)

@client.command()
async def admin(ctx):
    channel = client.get_channel(cfg_channel)
    str1 = '\n'.join(head_admins)
    str2 = '\n'.join(admins)
    str3 = '\n'.join(mods)
    await channel.send(
        f'***Administracja serwera {server_name}***\n'
        f'**Główni administratorzy:**\n'
        f'{str1}'
        f'\n**Administratorzy:**\n'
        f'{str2}'
        f'\n**Moderatorzy:**\n'
        f'{str3}'
    )

@client.command()
async def support(ctx):
    channel = client.get_channel(cfg_channel)
    str1 = '\n'.join(supporters)
    await channel.send(
        f'***Oto lista wspierających serwer {server_name}***\n'
        f'{str1}\n\n'
        f'Jeśli chcesz znaleźć się na tej liście koniecznie zajrzyj na kanał #wesprzyj_nas \n'
    )

@client.command()
async def cat(ctx):
    channel = client.get_channel(cfg_channel)
    cat = GetCat()
    await channel.send(
        f'{cat}'
    )

@client.command()
async def dog(ctx):
    channel = client.get_channel(cfg_channel)
    dog = GetReddit('dogpictures')
    await channel.send(
        f'{dog}'
    )

@client.command()
async def linuxmeme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('linuxmemes')
    await channel.send(
        f'{meme}'
    )

@client.command()
async def windowsmeme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('windowsmemes')
    await channel.send(
        f'{meme}'
    )

@client.command()
async def plmeme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('Polska_wpz')
    await channel.send(
        f'{meme}'
    )

@client.command()
async def meme(ctx):
    channel = client.get_channel(cfg_channel)
    meme = GetReddit('memes')
    await channel.send(
        f'{meme}'
    )

@client.command()
async def unixporn(ctx):
    channel = client.get_channel(cfg_channel)
    unixporn = GetReddit('unixporn')
    await channel.send(
        f'{unixporn}'
    )

@client.command()
async def wallpaper(ctx):
    channel = client.get_channel(cfg_channel)
    wp = GetWallpaper()
    await channel.send(
        f'{wp}'
    )

@client.command()
async def test():
    channel = client.get_channel(cfg_channel)
    embedVar = discord.Embed(title="Test", description="Testowy opis", color=0x00ff00)
    embedVar.add_field(name="Pole #1", value="Wartość pola #1", inline=False)
    embedVar.add_field(name="Pole #2", value="ęśąćż", inline=False)
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
            await channel.send(
                f'Hej!\nNowa wersja systemu operacyjnego **{os_3}** została wydana!\nAktualna wersja to: **{chk_os}**\nZachęcamy do aktualizacji systemu.\n'
            )
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
        await channel.send(
            f'Hej!\nPojawiła się nowa wersja Wine Stable!\nAktualna wersja to: **{chk_wine}!**\n'
        )
        config.set("gaming", "wine", chk_wine)
    if chk_wine_testing != cfg_wine_testing:
        await channel.send(
            f'Hej!\nPojawiła się nowa wersja Wine Testing!\nAktualna wersja to: **{chk_wine_testing}!**\n'
        )
        config.set("gaming", "wine_testing", chk_wine_testing)
    if chk_proton != cfg_proton:
        await channel.send(
            f'Hej!\nPojawiła się nowa wersja Proton!\nAktualna wersja to: **{chk_proton}!**\n'
        )
        config.set("gaming", "proton", chk_proton)
    if chk_proton_ge != cfg_proton_ge:
        await channel.send(
            f'Hej!\nPojawiła się nowa wersja Proton-GE!\nAktualna wersja to: **{chk_proton_ge}!**\n'
        )
        config.set("gaming", "proton_ge", chk_proton_ge)
    if chk_wine_ge != cfg_wine_ge:
        await channel.send(
            f'Hej!\nPojawiła się nowa wersja Wine-GE!\nAktualna wersja to: **{chk_wine_ge}!**\n'
        )
        config.set("gaming", "wine_ge", chk_wine_ge)
    if chk_wine_kronfourek != cfg_wine_kronfourek:
        await channel.send(
            f'Hej!\nPojawiła się nowa wersja Wine Kron4ek (Vanilla build)!\nAktualna wersja to: **{chk_wine_kronfourek}!**\n'
        )
        config.set("gaming", "wine_kronfourek", chk_wine_kronfourek)
    if chk_lutris != cfg_lutris:
        await channel.send(
            f'Hej!\nPojawiła się nowa wersja Lutris!\nAktualna wersja to: **{chk_lutris}!**\n'
        )
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
            await channel.send(
                f'Hej, użytkownicy kart graficznych NVidia!\nZostała wydana nowa wersja sterownika "New Features Branch".\nNazwa sterownika: {chk_nv_nfb_name}\nWersja: **{chk_nv_nfb_version}**\nData wydania: **{chk_nv_nfb_date}**\n'
            )
            config.set("video", "nvidia_nfb", chk_nv_nfb_version)
    if chk_nv_pb_version != cfg_nv_pb:
            await channel.send(
                f'Hej, użytkownicy kart graficznych NVidia!\nZostała wydana nowa wersja sterownika "Production Branch".\nNazwa sterownika: {chk_nv_pb_name}\nWersja: **{chk_nv_pb_version}**\nData wydania: **{chk_nv_pb_date}**\n'
            )
            config.set("video", "nvidia_pb", chk_nv_pb_version)
    with open('./psl_version_checker.ini', 'w') as configfile:
        config.write(configfile)


## init
if __name__ == '__main__':
    client.run(token)
