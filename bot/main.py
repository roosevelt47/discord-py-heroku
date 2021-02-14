import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.event
async def on_message(message):
    if message.author.bot:
    return
    message_str = message.content.lower()
    message_list = message_str.split()
    if "hello" in message.content.lower():
        await message.channel.send("Hey")
    elif "yo" in message.content.lower():
        await message.channel.send("yo")
    elif "gm" in message.content.lower():
        await message.channel.send("Good Morning")
    elif "gn" in message.content.lower():
        await message.channel.send("Good Night")
    elif "good morning" in message.content.lower():
        await message.channel.send("Good Morning !")
    elif "good night" in message.content.lower():
        await message.channel.send("Good Night !")
    elif "hey" in message.content.lower():
        await message.channel.send("Hello !")
    elif "sup" in message.content.lower():
        await message.channel.send("Sup")
    elif "hi" in message_list:
        await message.channel.send("Hello!")


if __name__ == "__main__":
    bot.run(TOKEN)
