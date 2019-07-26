import asyncio
import aiohttp
import discord
import json
import whois
from discord.ext import commands
with open("conf.json","r") as h:
    config = json.load(h)
c = commands.Bot(command_prefix=commands.when_mentioned_or("."))
c.remove_command('help')
extensions = ['osint']

@c.event
async def on_ready():
    print("Im ready")

@c.command()
async def help(ctx):
    h = discord.Embed(
        color=discord.Colour.green()
    )
    h.add_field(name="!sdns", value="Searches Subdomains Of Given Sites")
    h.add_field(name="!shost", value="Provides Information on given host")
    h.add_field(name="!ifconfig", value="Provides Info on a certain IP")
    await ctx.send(embed=h)




if __name__=='__main__':
    for extension in extensions:
        try:
            c.load_extension(extension)
        except Exception as error:
            print(f"{extension} cannot be loaded [{error}]")

c.run(conf['token'])
