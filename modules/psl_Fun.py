import json
from urllib import request

def GetCat():
    page = request.urlopen("http://aws.random.cat//meow")
    for entry in page:
        cats = json.loads(entry.decode("utf-8"))
    return cats["file"]

def GetWallpaper():
    page = request.urlopen("https://source.unsplash.com/random/1920x1080")
    return(page.geturl())

def GetReddit(subreddit):
    page = request.urlopen(f'https://meme-api.herokuapp.com/gimme/{subreddit}')
    for entry in page:
        meme = json.loads(entry.decode("utf-8"))
    return meme["url"]
