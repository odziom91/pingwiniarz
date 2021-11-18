import re
from urllib import request
from bs4 import BeautifulSoup

def GetVersion_Wine():
    wine = []
    page = request.urlopen("https://www.winehq.org/")
    soup = BeautifulSoup(page, features="html.parser")
    x = soup.findAll('a', attrs={'href' : re.compile(r'announce/[0-9]*\.[0-9]+')})
    for i in x:
        try:
            wine.append(re.search(r'[0-9].+',i.text).string)
        except Exception as e:
            print(str(e))
            pass
    return wine[0], wine[1]
    
def GetVersion_Lutris():
    page = request.urlopen("https://github.com/lutris/lutris/releases/latest")
    soup = BeautifulSoup(page, features="html.parser")
    output = soup.findAll('h1', attrs={'class' : 'd-inline mr-3'})
    lutris = output[0].text
    return lutris

def GetVersion_Proton():
    page = request.urlopen("https://github.com/ValveSoftware/Proton/releases/latest")
    soup = BeautifulSoup(page, features="html.parser")
    output = soup.findAll('h1', attrs={'class' : 'd-inline mr-3'})
    proton = output[0].text.split()
    return proton[1]

def GetVersion_Proton_GE():
    page = request.urlopen("https://github.com/GloriousEggroll/proton-ge-custom/releases/latest")
    soup = BeautifulSoup(page, features="html.parser")
    output = soup.findAll('h1', attrs={'class' : 'd-inline mr-3'})
    proton = output[0].text.split()
    return proton[0]

def GetVersion_Wine_GE():
    page = request.urlopen("https://github.com/GloriousEggroll/wine-ge-custom/releases/latest")
    soup = BeautifulSoup(page, features="html.parser")
    output = soup.findAll('h1', attrs={'class' : 'd-inline mr-3'})
    wine = output[0].text.split()
    return wine[0]

def GetVersion_Wine_Kronfourek():
    page = request.urlopen("https://github.com/Kron4ek/Wine-Builds/releases/latest")
    soup = BeautifulSoup(page, features="html.parser")
    output = soup.findAll('h1', attrs={'class' : 'd-inline mr-3'})
    wine = output[0].text
    return wine

### old version
# def GetVersion_Distrowatch(url):
#     distrowatch = []
#     page = request.urlopen(url)
#     for i, entry in enumerate(page):
#         if i < 3:
#             version = entry.decode("utf-8").replace("<br>", " ").replace("\n", "")
#             distrowatch.append(version)
#     return distrowatch

def GetVersion_Distrowatch_OS(os, os_entry):
    distrowatch = []
    page = request.urlopen(f'https://distrowatch.com/distro/{os}/{os}-versions.txt')
    for i, entry in enumerate(page):
        version = entry.decode("utf-8").replace("<br>", " ").replace("\n", "")
        distrowatch.append(version)
    return distrowatch[os_entry]