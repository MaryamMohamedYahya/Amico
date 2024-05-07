import discord
import decouple
from discord.ext import commands

Amico = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@Amico.event
async def on_member_join(member):
     welcome_channel=Amico.get_channel({1237442411920228404})
     message="Welcome on Board! {member.name}"
     welcome_channel.send(message)
     member.send(message)

@Amico.event
async def on_message(message):
     if message.author.bot:
          return
     await message.reply("😀")
     await message.channel.send("😐")

Amico.run(decouple.config("TOKEN"))