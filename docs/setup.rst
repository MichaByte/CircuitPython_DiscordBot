Setup
------------

How to set up


1. Set up a discord bot.

  a. Go to https://discord.com/developers and make a new application.
  b. Type in the name for the bot (This will not be visible) for the application name. Once it's created, click Bot on the side and click Add Bot.
  c. Copy the **bot token** and save it for later. If you want, change the profile picture and username of your bot user. Keep that picture on your computer for a step later.
  d. Click the OAuth2 section and check the checkbox that says Bot in the Scopes section. Check the checkbox that says Administrator in the Bot Permissions section. Copy the URL in the scopes section and save it for later.

2. Set up the server.

  a. Open Discord, scroll down your Server list, and click the Plus sign.
  b. Click Create my Own.
  c. Enter a name that you are comfortable with other people seeing. If you want, add an icon.
  d. Go to the link from step 1d. Select your new server from the dropdown and click Continue.
  e. Leave the box Administrator checked and click Authorize. Then, complete the Captcha.

3. Set up webhook.

  a. Hover over the channel you want your bot to use and click the gear.
  b. Go to Integrations.
  c. Click Create Webhook.
  d. Enter the same name and use the same image from before. This isn't required, but it will maintain consistency with your bot.
  e. Click Copy URL and save it for later.

4. Finish up.

  a. Click the gear next to your Discord username.
  b. Click Appearance on the side menu.
  c. Scroll down and turn on Developer Mode.
  d. Exit the server settings by clicking on the X. Right-click the channel that you want your bot to "live" in, and you will see a new option - Copy ID! Click that and save it for later,
  e. Using the API key, channel ID, and webhook URL from earlier, write your CircuitPython code according to the documentation!
