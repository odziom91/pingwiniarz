import datetime
import discord
from discord.ext import commands, tasks
import feedparser

class psl_RssParser(commands.Cog):
    def __init__(self, client, channel_id, embed_color):
        try:
            self.client = client
            self.embed_color = embed_color
            self.channel_id = channel_id
            self.RssParser.start()
        except Exception as e:
            print(str(e))

    @tasks.loop(seconds=3600)
    async def RssParser(self):
        try:
            feeds = [
                ("https://lowcygier.pl/darmowe/feed/","lowcy_darmowe","Łowcy Gier - Gry za darmo"),
                ("https://lowcygier.pl/promocje-cyfrowe/feed/","lowcy_promo_cyfrowe","Łowcy Gier - Promocje cyfrowe"),
                ("https://lowcygier.pl/promocje-pudelkowe/feed/","lowcy_promo_pudelkowe","Łowcy Gier - Promocje pudełkowe")
            ]
            for feed in feeds:
                channel = self.client.get_channel(self.channel_id)
                feed_rss, feed_name, feed_longname = feed
                feed_readfile = open(f'parser/{feed_name}.txt', 'r').read()
                NewsFeed = feedparser.parse(f'{feed_rss}')
                entry = NewsFeed.entries[0]
                if entry.title != feed_readfile:
                    embed = discord.Embed(title=f'{feed_longname}', description=f'{entry.title}', color=self.embed_color, timestamp=datetime.datetime.utcnow())
                    await channel.send(embed=embed)
                    feed_write = open(f'parser/{feed_name}.txt', 'w')
                    feed_write.write(entry.title)
                    feed_write.close()
        except Exception as e:
            print(str(e))