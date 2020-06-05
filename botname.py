import discord

class botname(discord.Client):
  async def on_ready(self):
      print("Bot is online and connected to Discord")
      print("Hello, I am botname")

  async def on_message(self, message):
      if message.content.startswith('!PING'):
          userID = message.author.id
          await message.channel.send('@{} Pong!').format(userID)

      if message.content.startswith('!SAY'):
          arg = message.content
          await message.channel.send('{}').format(arg)

client = botname()
client.run('NzE2NDQyNTEwNDIzMjI4NDk2.XtMbNQ.ogYbexa7FuqvuH8Z_vBvzlFEZMQ')
