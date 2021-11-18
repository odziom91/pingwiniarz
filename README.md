# pingwiniarz
Bot Discord dla społeczności "Polska Społeczność Linuxa"

## Wymagane moduły
- Discord
- BeautifulSoup4

## Inicjacja
1. Sklonuj repozytorium.
2. Utwórz plik psl_config.ini - skorzystaj z pliku example_psl_config.ini
3. Uzupełnij wszystkie dane - wraz z tokenem wygenerowanym w środowisku deweloperskim Discord.
4. Uruchom przez komendę python3 ./psl_bot.py

## psl_config.ini - dokumentacja
Poniżej opisane są poszczególne opcje:

```
[config]
bot_name = tu wpisz nazwę bota, będzie ona się pojawiać w sekcji ;pomoc
server_name = tu wpisz nazwę serwera, na którym postawiony jest bot
channel_id = wprowadź ID kanału tekstowego, na którym będą pojawiać się treści z bota
godfather = tu wpisz dane o założycielu serwera - może to być nick. Można wpisać kilku rozdzielając przecinkiem
head_admins = tu wpisz nicki głównych administratorów - każdy oddzielony przecinkiem
admins = tu wpisz nicki administratorów - każdy oddzielony przecinkiem
mods = tu wpisz nicki moderatorów - każdy oddzielony przecinkiem
supporters = tu wpisz nicki osób wspierających - każdy oddzielony przecinkiem
token = tu należy wkleić wygenerowany w środowisku deweloperskim Discorda token
```

## Lista komend
```
Komendy dotyczące serwera:
;admin - aktualny zespół administracji i moderatorów
;support - lista wspierających serwer

```

```
Komendy dotyczące Linuksa:
;linver - informacja o aktualnie dostępnych wersjach wybranych dystrybucji Linuksa
;gaming - informacja o aktualnie dostępnych wersjach oprogramowania dla graczy - Lutris, Wine, Proton, etc.
;pobierz - lista hiperłączy dla wybranych dystrybucji do pobrania

```

```
Pozostałe:
;cat - losuj słodkiego kota
;dog - losuj słodkiego psa
;linuxmeme - losuj mema o Linuksie
;windowsmeme - losuj mema o Windowsie
;plmeme - losuj polskiego mema
;meme - losuj zagranicznego mema
;unixporn - losuj desktop
;wallpaper - inspiracja na tapetę
```