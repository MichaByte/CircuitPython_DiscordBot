# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 2231puppy for Project Stida
#
# SPDX-License-Identifier: MIT
"""
`adafruit_discordbot`
================================================================================

A very simple Discord API for CircuitPython


* Author(s): 2231puppy
"""

# imports
import json
import requests

class DiscordBot:
    """DiscordBot Class"""
    def __init__(self, key, webhook):
        self.key = key
        self.r = None
        self.jsonified_r = None
        self.webhook = webhook
        self.embed = None

    def get_msg(self, channel, msg, get_author=False):
        """Gets a message from the channel. Use 0 for latest. Specify True at the end of the function to return the username of the sender instead."""
        self.r = requests.get(
            "https://discord.com/api/v8/channels/" + channel + "/messages",
            headers={"Authorization": "Bot " + self.key},
        )
        self.jsonified_r = json.loads(self.r.content.decode("utf-8"))
        if get_author==True:
            return self.jsonified_r[msg]["author"]["username"]+"#"+str(self.jsonified_r[msg]["author"]["discriminator"])
        else:
            return self.jsonified_r[msg]["content"]

    def send_embed(self, title, content, color=0):
        '''Sends an embed message. Use https://www.shodor.org/stella2java/rgbint.html to generate the color integer.'''
        self.embed = '''{"embeds": [{"title": "'''+title+'''","description": "'''+content+'''","color": '''+str(color)+'''}]}'''
        requests.post(self.webhook, {"payload_json" : self.embed})

    def send_msg(self, msg, tts=False):
        """Sends a webhook message. Specify True at the end for TTS."""
        requests.post(self.webhook, {"content" : msg, "tts" : tts})

