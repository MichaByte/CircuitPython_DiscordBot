# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
from adafruit_discordbot import DiscordBot

key = "YOUR_API_KEY"
webhook = "YOUR_WEBHOOK_URL"
channel = "YOUR_CHAN_ID"

bot = DiscordBot(key, webhook)

bot.send_msg("Hello, world!")

bot.get_msg(channel, 0)
