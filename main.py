#!/usr/bin/python3
import feedparser
from time import sleep
from discord import Webhook, RequestsWebhookAdapter
import configparser
import json

# import the discord token & id
_config = configparser.ConfigParser()
_config.read("config.ini")

# connect to discord server
webhook = Webhook.partial(int(_config.get("discord", "id")),
                          _config.get("discord", "token"),
                          adapter=RequestsWebhookAdapter())

url = ["https://www.apkmirror.com/feed/"]
time_file = "time.json"

# set-up the previous time
TIME = dict()
try:
    TIME = json.load(open(time_file, "r"))
except FileNotFoundError:
    file = open(time_file, "w")  # Create a file to save time afterwards
    file.close()


def feed(update: feedparser.util.FeedParserDict):
    """ parse the update from RSS """
    for post in update.entries:
        webhook.send(f"{post.title}\n{post.link}\n{post.published}",
                     username=update.feed.title)
        sleep(1)
        # print(f"{post['title']}\n{post['link']}\n{post['published']}")


if __name__ == '__main__':
    try:
        while True:
            print(TIME)
            update = feedparser.parse(url)

            if update.bozo_exception:
                print(update.bozo_exception)
                exit(1)

            print(update)
            print(update.feed.updated)
            if update.feed.updated != TIME:
                feed(update)
                TIME = update.feed.updated
            print(TIME)
            sleep(60)
    finally:
        with open("time.txt", "w") as file:
            file.write(TIME)  # save the time to a file if something went wrong
