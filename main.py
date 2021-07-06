#!/usr/bin/python3
import feedparser
from time import sleep
from discord import Webhook, RequestsWebhookAdapter
import configparser

# import the discord token & id
_config = configparser.ConfigParser()
_config.read("config.ini")

# connect to discord server
webhook = Webhook.partial(int(_config.get("discord", "id")),
                          _config.get("discord", "token"),
                          adapter=RequestsWebhookAdapter())

url = "https://apkcombo.com/latest-updates/feed"

# set-up the previous time
try:
    TIME = open("time.txt", "r").read()
except FileNotFoundError:
    TIME = ""
    file = open("time.txt", "w")  # Create a file to save time afterwards
    file.close()


def feed(update: feedparser.util.FeedParserDict):
    """ parse the update from RSS """
    for post in update.entries:
        webhook.send(f"{post.title}\n{post.link}\n{post.published}",
                     username=update.feed.title)
        # print(f"{post['title']}\n{post['link']}\n{post['published']}")


if __name__ == '__main__':
    try:
        while True:
            update = feedparser.parse(url)
            if update.feed.updated != TIME:
                feed(update)
                TIME = update.updated
            print(TIME)
            sleep(60)
    finally:
        with open("time.txt", "w") as file:
            file.write(TIME)  # save the time to a file if something went wrong
