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

First, create a bot and a webhook for your server (Read my ReadTheDocs). Then, import the library like so::

    import board
    import busio
    from digitalio import DigitalInOut
    import adafruit_esp32spi.adafruit_esp32spi_socket as socket
    from adafruit_esp32spi import adafruit_esp32spi

    # Get wifi details and more from a secrets.py file
    try:
        from secrets import secrets
    except ImportError:
        print("WiFi secrets are kept in secrets.py, please add them there!")
        raise
    # If you are using a board with pre-defined ESP32 Pins:
    esp32_cs = DigitalInOut(board.ESP_CS)
    esp32_ready = DigitalInOut(board.ESP_BUSY)
    esp32_reset = DigitalInOut(board.ESP_RESET)

    # If you have an AirLift Shield:
    # esp32_cs = DigitalInOut(board.D10)
    # esp32_ready = DigitalInOut(board.D7)
    # esp32_reset = DigitalInOut(board.D5)

    # If you have an AirLift Featherwing or ItsyBitsy Airlift:
    # esp32_cs = DigitalInOut(board.D13)
    # esp32_ready = DigitalInOut(board.D11)
    # esp32_reset = DigitalInOut(board.D12)

    # If you have an externally connected ESP32:
    # NOTE: You may need to change the pins to reflect your wiring
    # esp32_cs = DigitalInOut(board.D9)
    # esp32_ready = DigitalInOut(board.D10)
    # esp32_reset = DigitalInOut(board.D5)

    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)


``from adafruit_discordbot import DiscordBot``


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
