import discord
import json
import aiohttp
import asyncio
import whois
from discord.ext import commands

class Osint(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    async def on_message_delete(self, message):
        await ctx.send(message.channel, "Message Deleted")

    @commands.command()
    async def ifconfig(self, ctx, arg1):
        url = f"http://ip-api.com/json/{arg1}"
        ip = discord.Embed(
        color=discord.Colour.purple()
        )
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            ip.add_field(name="ISP", value=response['isp'])
            ip.add_field(name="Country", value=response['country'])
            ip.add_field(name="State", value=response['region'])
            ip.add_field(name="Area Code", value=response['zip'])
            ip.add_field(name="ASN", value=response['as'])
            await ctx.send(embed=ip)

    @commands.command()
    async def shost(self, ctx, arg1):
        url = f"https://api.shodan.io/shodan/host/{arg1}?key="
        shop = discord.Embed(
        color=discord.Colour.red()
        )
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            shop.add_field(name="ISP", value=response['isp'])
            shop.add_field(name="Country", value=response['country'])
            shop.add_field(name="State", value=response['region'])
            shop.add_field(name="Area Code", value=response['area_code'])
            shop.add_field(name="ASN", value=response['as'])
            shop.add_field(name="Banner", value=response['banner'])
            await ctx.send(embed=shop)

    @commands.command()
    async def sdns(self, ctx, arg1):
        url = f"https://api.shodan.io/dns/domain/{arg1}?key="
        sho = discord.Embed(
        color=discord.Colour.red()
        )
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            sho.add_field(name="Domain", value=response['domain'])
            sho.add_field(name="Tags", value=response['tags'])
            sho.add_field(name="Subdomain", value=response['subdomain'])
            sho.add_field(name="DNS Type", value=response['type'])
            sho.add_field(name="SD Link", value=response['value'])
            await ctx.send(embed=sho)

    @commands.command()
    async def whos(self, ctx, arg1):
        ws = discord.Embed(
            discord.Colour.red()
            )
        w = whois.whois(arg1)
        ws.add_field(name="info", value=w)
        await ctx.send(embed=ws)


def setup(client):
    client.add_cog(Osint(client))
