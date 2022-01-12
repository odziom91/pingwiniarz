# Pingwiniarz
Bot Discord dla społeczności "Polska Społeczność Linuxa"

## O "Pingwiniarzu"
Głównym zadaniem "Pingwiniarza" jest informowanie użytkowników Discorda o nowych wersjach kernela, dystrybucji Linuksa oraz oprogramowania.

Dodatkowo dzięki zaimplementowanym funkcjom możliwe jest sprawdzenie tych informacji w dowolnym momencie. Jako smaczek pojawiły się tu również parsery dla zdjęć z kilku portali.

Bot cały czas jest w rozbudowie.

## Systemy operacyjne, które obsługuje bot
- Ubuntu
- Pop!_OS
- KDE Neon
- Elementary OS
- Linux Mint
- Zorin OS
- Solus
- Garuda Linux
- EndeavourOS
- Manjaro Linux
- MX Linux
- Fedora
- OpenSuse
- Arch Linux
- Void Linux
- Gentoo Linux
- Slackware
- Linux From Scratch
- Qubes OS
- NixOS

Lista systemów operacyjnych może ulec zmianie.

## Oprogramowanie, które obsługuje bot
- Lutris
- Wine
- Proton
- Proton-GE
- Wine-GE
- Wine Kron4ek

W przyszłości dodanie zostanie wsparcie dla Luxtorpeda i innego softu.

## Kernel.org

Bot wspiera odpytywanie strony internetowej https://www.kernel.org/ w celu pobrania informacji o najnowszych wersjach kernela.

Gałęzie:
- mainline
- stable
- longterm

## Wymagane moduły
- Discord
- BeautifulSoup4

## Inicjacja
1. Sklonuj repozytorium.
2. Utwórz plik psl_config.ini - skorzystaj z pliku example_psl_config.ini
3. Uzupełnij wszystkie dane - wraz z tokenem wygenerowanym w środowisku deweloperskim Discord.
4. Uruchom w tle przez komendę ```nohup python3 ./psl_bot.py &```
   
   Możesz również wykorzystać komendę ```screen```.

## psl_config.ini - dokumentacja
Poniżej opisane są poszczególne opcje:

```
[config]
bot_name = tu wpisz nazwę bota, będzie ona się pojawiać w sekcji ;pomoc
server_name = tu wpisz nazwę serwera, na którym postawiony jest bot
channel_id = wprowadź ID kanału tekstowego, na którym będą pojawiać się treści z bota
suggestions_id = wprowadź ID kanału tekstowego z sugestiami
rss_id = wprowadź ID kanału tekstowego dla parsera RSS (wspierane: Łowcy Gier)
error_id = wprowadź ID kanału tekstowego, na którym będą wypisywane błędy bota
godfather = tu wpisz dane o założycielu serwera - może to być nick.
head_admins = tu wpisz id grupy głównych administratorów
admins = tu wpisz id grupy administratorów
mods = tu wpisz id grupy moderatorów
supporters = tu wpisz id grupy wspierających
token = tu należy wkleić wygenerowany w środowisku deweloperskim Discorda token
```

## Lista komend
```
Komendy dotyczące serwera:
;admin - aktualny zespół administracji i moderatorów
;support - lista wspierających serwer
;sugestia <tekst sugestii> - zgłoś sugestię dot. serwera, działa tylko na kanale #propozycje_sugestie
;userinfo [użytkownik] - sprawdź informacje o sobie (bez parametru) lub użytkowniku (z parametrem)
```

```
Komendy dotyczące Linuksa:
;linver - informacja o aktualnie dostępnych wersjach wybranych dystrybucji Linuksa
;kernel - informacja o aktualnie dostępnych wersjach kernela Linuksa
;gaming - informacja o aktualnie dostępnych wersjach oprogramowania dla graczy - Lutris, Wine, Proton, etc.
;pobierz - lista hiperłączy dla wybranych dystrybucji do pobrania
;nvidia - informacja o sterownikach wideo kart graficznych NVidia

```

```
Pozostałe:
;cat - losuj słodkiego kota
;dog - losuj słodkiego psa
;linuxmeme - losuj mema o Linuksie
;windowsmeme - losuj mema o Windowsie
;plmeme - losuj polskiego mema
;meme - losuj zagranicznego mema
;papameme - "po maturze chodziliśmy na kremówki" ;) - memy z API by Mopsior
;unixporn - losuj desktop
;wallpaper - inspiracja na tapetę
```

```
Dla administratorów:
;tw tekst - zamienia tekst na ikony z literami
```