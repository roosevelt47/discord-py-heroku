import os
from discord.ext import commands

bot = commands.Bot(command_prefix=";")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id}) OKAYYYYYYYYYYYYYYYYY")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

'''
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    message_str = message.content.lower()
    message_list = message_str.split()
    if "hello" in message_list:
        await message.channel.send("Hey")
    elif "yo" in message_list:
        await message.channel.send("yo")
    elif "gm" in message_list:
        await message.channel.send("Good Morning")
    elif "gn" in message_list:
        await message.channel.send("Good Night")
    elif "good morning" in message_list:
        await message.channel.send("Good Morning !")
    elif "good night" in message_list:
        await message.channel.send("Good Night !")
    elif "hey" in message_list:
        await message.channel.send("Hello !")
    elif "sup" in message_list:
        await message.channel.send("Sup")
    elif "hi" in message_list:
        await message.channel.send("Hello!")
'''

@bot.command()
async def gapply(messages, email):
    author = messages.author
    await messages.message.delete()
    reply = f'Your email has been recorded {author.mention}!'
    await messages.channel.send(reply)
    info = f'New request by {author.mention} Email - {email} userid -'
    
    await messages.channel.send(info)
    print(reply)

if __name__ == "__main__":
    bot.run(TOKEN)
