# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 2231puppy for Project Stida
#
# SPDX-License-Identifier: MIT
"""
`adafruit_discordbot`
================================================================================

A very simple Discord API for CircuitPython


* Author(s): 2231puppy

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library
dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports
import json
import adafruit_requests as requests
__version__ = "1.1.3"
__repo__ = "https://github.com/2231puppy/CircuitPython_DiscordBot.git"

class DiscordBot:
    """DiscordBot Class"""
    def __init__(self, key, webhook, socket, esp):
        self.key = key
        self.r = None
        self.jsonified_r = None
        self.webhook = webhook
        self.embed = None
        requests.set_socket(socket, esp)
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
        requests.post(self.webhook, json={"payload_json" : self.embed})

    def send_msg(self, msg, tts=False):
        """Sends a webhook message. Specify True at the end for TTS."""
        requests.post(self.webhook, json={"content" : msg, "tts" : tts})

