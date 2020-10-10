Introduction
============

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


A very simple Discord API for CircuitPython

Sadly, I couldn't figure out how to send messages with bots without something complex (feel free to leave an issue if you know how), so to send messages, I utilize a webhook.

Whenever I mention the Channel ID, you will need to right click on the Discord channel and click Copy ID. If it doesn't show itself, fear not! Open your Discord settings, go to Appearence, scroll down, turn on Development Mode, and try again.

Dependencies
=============
This library depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `JSON (built-in)`
* Either `Adafruit Requests` or `Python requests`
Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

Usage Example
=============

First, create a bot and a webhook for your server (Google is your friend, more tutorials later). Then, import the library like so:

``from discordbot import DiscordBot``

And to test it:

``bot=DiscordBot(YOUR_BOT_TOKEN, YOUR_WEBHOOK_URL)``

``bot.send_msg('Hello, world!')``

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/2231puppy/Adafruit_CircuitPython_DiscordBot/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
