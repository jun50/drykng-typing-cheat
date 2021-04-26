import discord

client = discord.Client()

@client.event
async def on_ready():
    print("ready!")

@client.event
async def on_message(message):
    if message.author.id == 508166063473688577 and message.embeds[0].author.name == "タイピングゲーム":
        await message.channel.send(message.embeds[0].description.split("\n")[-1].replace(" ", ""))

client.run("token")
