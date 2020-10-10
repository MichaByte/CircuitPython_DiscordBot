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

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports
import adafruit_requests as requests
import json
__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/2231puppy/Adafruit_CircuitPython_DiscordBot.git"

class DiscordBot:
    def __init__(self, key, webhook):
        self.key = key
        self.r=None
        self.jsonified=None
        self.webhook=webhook
    def get_msg(self, channel, msg):
        self.r=requests.get("https://discord.com/api/v8/channels/"+channel+"/messages", headers={'Authorization' : 'Bot '+self.key})
        self.jsonified_r=json.loads(self.r.content.decode('utf-8'))
        return self.jsonified_r[msg]['content']
    def send_msg(self, msg):
        requests.post(self.webhook, {'content' : msg})
