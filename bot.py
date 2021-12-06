###################################################
try:
  import os
  from Resources import *
  import json
  import sys
  from sys import platform
  from threading import Thread
  import functools
  import discord
  import requests
  import aiohttp
  import random
  from discord import Webhook, AsyncWebhookAdapter
  from discord.ext import commands
  import httpx
  from geolite2 import geolite2
  import aioconsole
  import asyncio
  import time
  import getpass
  from colorama import Fore as coloring, init
  init()
  import base64
except Exception as e:
  handler(e).efilter()
  os._exit(1)
###################################################
if os.name == "nt":
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
###################################################
# Bot Panel #
##################################################
with open('user.json') as userjs:
    userjson = json.load(userjs)
    global sned
    sned = userjson.get('spam')
    global prefix
    prefix = userjson.get('prefix')
    global status
    status = userjson.get("status")
    global hook
    hook = False
    global user 
    user = getpass.getuser()
    global stat 
    stat = status.lower()
##########################################################
ments=discord.AllowedMentions(
        users=True,
        everyone=True,
        roles=True,
        replied_user=False,
    )
intents = discord.Intents().all()
roover = commands.Bot(self_bot=True, intents=intents, command_prefix=commands.when_mentioned_or(prefix), case_insensitive=True,  strip_after_prefix=True, allowed_mentions=ments)
token = os.getenv('TOKEN')
userp = os.getenv('USER')
##########################################################
# Bot Events #
##########################################################
@roover.event
async def on_ready():
  await roover.wait_until_ready()
  class omugus:
    the_bot = roover.user.name
    version = foundation.__version__
  tascii(omugus)
  try:
    time.sleep(2) 
    if stat == "true":
      await roover.change_presence(activity=discord.Streaming(name='🔋 | 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝙗𝙮 𝙍𝙤𝙤𝙫𝙚𝙧𝘾𝙤𝙧𝙙', url='https://www.twitch.tv/')) 
    elif stat == "false":
      pass
    else:
      os.system("cls" if os.name == "nt" else "clear")
      print(f"\nCritical error encountered. Invalid user input entered.\nJson values can only be true or false.")
      os._exit(4)
  except Exception as e:
    handler(e).efilter()
    os._exit(5)
  time.sleep(1.5)
  while True:
      fuck = await aioconsole.ainput(f"""\n{coloring.BLUE}┌──{coloring.BLUE}「{coloring.RED}{user}[Ω]RooverNET{coloring.BLUE}」-[{coloring.YELLOW}!{coloring.BLUE}]{coloring.WHITE}:{coloring.BLUE}
└─{coloring.MAGENTA}${coloring.WHITE}: """)
      print(f"{coloring.BLUE}─────────────────────────────")
      inp = str(fuck)
      work(inp).parse() # Loop automatically waits for takeuin to finish before asking for more input (To my convenience).
      
@roover.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
      return
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
      em = discord.Embed(title=f"Invalid Command Called:", description=f"{ctx.message.content}")
      em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
      em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
      await ctx.send(embed=em, delete_after=5)
    else:
        em = discord.Embed(title=f"An Error Has Occurred:", description=f"{error}.")
        em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
        em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
        await ctx.send(embed=em, delete_after=10)
##########################################################
# Bot Commands #
##########################################################
@roover.command(name="Presence", descrpition="Changes account status.")
@commands.cooldown(1, 20)
async def presence(ctx, *, stat):
  await ctx.message.delete()
  game = discord.Game(stat)
  await roover.change_presence(status=discord.Status.idle, activity=game)
##########################################################
@roover.command(name="Ping", description="Returns bot latency via embed.")
@commands.cooldown(1, 5)
async def ping(ctx):
  eme = discord.Embed(color=0x0394fc,title="Latency:", colour = ctx.bot.user.colour, timestamp=ctx.message.created_at)
  eme.add_field(name="Ping:", value=f"{roover.latency}", inline=False)
  eme.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}") 
  eme.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
  await ctx.send(embed=eme, delete_after=60)
##########################################################
@roover.command(name="Base64_Encode", aliases=["baseen", "b64", 'encode'], description="Converts user argument to Base64.")
@commands.cooldown(1, 3)
async def encode(ctx, *, message=None):
        await ctx.message.delete() # Deletes command message.
        if message is None: # If no argument given it sends the error embed.
            em = discord.Embed(title="No Argument Provided")
            em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
            em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
            await ctx.send(embed=em, delete_after=5) # Deletes after 5 seconds.
            return
        else:
          mom = base64.b64encode(str(message).encode("utf-8"))
          mom2 = str(mom, "utf-8")
          em = discord.Embed(color=0x0394fc,title="Encoded Message:", colour = ctx.bot.user.colour, timestamp=ctx.message.created_at)
          em.add_field(name="Message", value=f"{message}", inline=False)
          em.add_field(name="Encoded Message", value=f"{mom2}", inline=False)
          em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}") 
          em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
          await ctx.send(embed=em, delete_after=60)
###################################################
@roover.command(name="Base64_Decode", aliases=['basede','b64d', 'decode'], description="Decodes user argument from Base64.")
@commands.cooldown(1, 3)
async def decode(ctx, *, message=None):
        await ctx.message.delete()
        if message is None: # If no argument given it sends the error embed.
            em = discord.Embed(title="No Argument Provided")
            em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
            em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
            await ctx.send(embed=em, delete_after=5) # Deletes after 5 seconds.
            return
        else:
          roover_daddy = base64.b64decode(str(message).encode("utf-8"))
          mom3 = str(roover_daddy, "utf-8")
          emy = discord.Embed(color=0x0394fc,title="Decoded Message:", colour = ctx.bot.user.colour, timestamp=ctx.message.created_at)
          emy.add_field(name="Message", value=f"{message}", inline=False)
          emy.add_field(name="Decoded Message", value=f"{mom3}", inline=False)
          emy.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
          emy.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
          await ctx.send(embed=emy, delete_after=30)
###################################################
@roover.command(name="Credits", description="Bot credits.")
@commands.cooldown(1, 5)
async def credits(ctx):
        await ctx.message.delete()
        em = discord.Embed(title="**RooverCord**", description="\n \n Join: https://discord.gg/ANDUDHXMUC")
        em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
        em.set_image(url="https://media.discordapp.net/attachments/902278924673904670/909889142157094942/roover3.gif?width=457&height=457")
        em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿 𝗮𝗻𝗱 𝗦𝗵𝗲𝗹𝗹")
        await ctx.send(embed=em, delete_after=60)
###################################################
@roover.command(title="Tox", description="Shitty massreport that will never work :).")
async def tox(ctx, msgid):
    await ctx.message.delete()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
      }
    guildid = ctx.message.guild.id
    channid = ctx.message.channel.id
    reason = 1
    payload = {
    'channel_id': channid,
    'guild_id': guildid,
    'message_id': msgid,
    'reason': reason
    }
    while True:
      try:
        httpx.post(f"https://discord.com/api/v9/report", headers=headers, json=payload)
      except Exception as e:
        handler(e).efilter()
        break
###################################################
@roover.command(name="Gcleave", description="Leaves all gcs.")
async def gcleave(ctx):
  for channel in roover.private_channels:
    if isinstance(channel, discord.GroupChannel):
      await channel.leave()
###################################################
@roover.command(name="Webjack", description="Spams all guild webooks.")
async def webjack(ctx):
  for i in range(30):
    for w in await ctx.guild.webhooks():
      try:
        await w.send(sned)
      except:
        pass
###################################################
@roover.command(name="Uncache", description="Fully resets the bot and errorcache.")
@commands.cooldown(1, 30)
async def uncache(ctx):
  await ctx.message.delete()
  if sys.platform != "linux" or "linux2":
    os.remove("Resources/utils/data/errorcache.txt")
    open("Resources/utils/data/errorcache.txt", "w+").close()
  else:
    os.remove("Resources/utils/data/errorcache.txt")
    time.sleep(1)
    os.mknod("Resources/utils/data/errorcache.txt")
###################################################
@roover.command(name="GeoIP", description="IP Information.", ignore_extra=False)
async def geoip(ctx, ipaddr: str):
        await ctx.message.delete()
        reader = geolite2.reader()
        location = reader.get(ipaddr)
        a=(location['city']['names']['en'])
        b=(location['continent']['names']['en'])
        c=(location['country']['names']['en'])
        g=(location['subdivisions'][0]['names']['en'])
        em = discord.Embed(color=0x0394fc,title="Decoded Message:", colour = ctx.bot.user.colour, timestamp=ctx.message.created_at)
        em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
        em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
        em.add_field(name="City", value=a, inline=True)
        em.add_field(name="Continent", value=b, inline=True)
        em.add_field(name="Country", value=c, inline=True)
        em.add_field(name="Subdivision", value=g, inline=True)
        await ctx.send(embed=em, delete_after=60)   
###################################################
@roover.command(name="Guilddm", description="Mass dms members of the guild.")
@commands.cooldown(1, 30)
async def guilddm(ctx, serverid, *, mesag):
  await ctx.message.delete()
  if serverid is None:
    for member in ctx.guild.members:
      try:
        cunt = httpx.post("https://discord.com/api/v9/users/@me/channels", json={ 'recipients': [member.id]}, headers={'authorization': token})
        dmid = (cunt.json()['id'])
        httpx.post(f"https://discord.com/api/v9/channels/{dmid}/messages", headers={'authorization':token}, json={"content":mesag, 'tts':'false'})
      except:
        pass
    em = discord.Embed(title=f"Command Completed:", description=f"DMed as many users as possible!")
    em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
    em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
    await ctx.send(embed=em, delete_after=10)
  else:
    try:
      targer = roover.get_guild(int(serverid))
      for member in targer.members:
        try:
          cunt = httpx.post("https://discord.com/api/v9/users/@me/channels", json={ 'recipients': [member.id]}, headers={'authorization': token})
          dmid = (cunt.json()['id'])
          httpx.post(f"https://discord.com/api/v9/channels/{dmid}/messages", headers={'authorization':token}, json={"content":mesag, 'tts':'false'})
        except:
          pass
      em = discord.Embed(title=f"Command Completed:", description=f"DMed as many users as possible!")
      em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
      em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
      await ctx.send(embed=em, delete_after=10)
    except:
      em = discord.Embed(title=f"An Error Has Occurred:", description=f"Invalid ID entered.")
      em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
      em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
      await ctx.send(embed=em, delete_after=10)
###################################################
@roover.command(name="Clear", description="Clears a chat, but only your messages.")
@commands.cooldown(1, 13)
async def clear(ctx):
  async for message in ctx.message.channel.history(limit=None):
    try:
      await message.delete()
    except:
      pass
###################################################
@roover.command(name="Threadspam", description="Mass creates threads on a specific channel.")
@commands.cooldown(1, 13)
@commands.guild_only()
async def threadspam(ctx, munker, tired=None):
    await ctx.message.delete()
    if tired is None:
          async for message in ctx.channel.history(limit=None):
              s = httpx.post(f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages/{message.id}/threads", headers={'authorization':token}, json={'name':munker})
              time.sleep(.6)
              if s.status_code == 429:
                time.sleep(.2)
                continue
              elif s.status_code == 204 or 200:
                continue
              else:
                break
    else:
      munke = int(tired)
      try:
        shelly = roover.get_channel(munke)
        async for message in shelly.history(limit=None):
              s = httpx.post(f"https://discord.com/api/v9/channels/{shelly.id}/messages/{message.id}/threads", headers={'authorization':token}, json={'name':munker})
              time.sleep(.6)
              if s.status_code == 429:
                time.sleep(.2)
                continue
              elif s.status_code == 204 or 200:
                continue
              else:
                break
      except:
        pass
###################################################
chans = []
def delchan(obama):
    try:
      httpx.delete(f"https://discord.com/api/v9/channels/{obama}", headers={'authorization':token})
    except:
      pass

@roover.command(name="Seize", description="Nukes a specified server.")
@commands.cooldown(1, 120)
async def seize(ctx, sid=None):
  await ctx.message.delete()
  if sid is None:
    for channel in ctx.guild.channels:
      chans.append(str(channel.id))
    for obama in chans:
      silly = functools.partial(delchan, obama)
      Thread(target=silly).start()
    try: 
      role = discord.utils.get(ctx.guild.roles, name = "@everyone")
      await role.edit(permissions = discord.Permissions.all()) 
    except: 
      pass
    try:
      await ctx.guild.edit(name=f"Razed by {userp} | {ctx.guild.name}")
    except:
      pass
    for member in ctx.guild.members:
      try:
        member.ban(reason="Nuked")
      except:
        pass
    for i in range(40):
      try:
        await ctx.guild.create_text_channel("razed")
      except:
        pass
    for chany in ctx.guild.channels:
        webhook = await chany.create_webhook(name={userp})
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
            for i in range(1):
              await webhook.send(sned)
  else:
    guild = roover.get_guild(int(sid))
    for channel in guild.channels:
      chans.append(str(channel.id))
    for obama in chans:
      silly = functools.partial(delchan, obama)
      Thread(target=silly).start()
    try: 
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = discord.Permissions.all()) 
    except: 
      pass
    try:
      await guild.edit(name=f"Razed by {userp} | {guild.name}")
    except:
      pass
    for member in guild.members:
      try:
        member.ban(reason="Nuked")
      except:
        pass
    for i in range(40):
      try:
        await guild.create_text_channel("nuked")
      except:
        pass
    for chany in guild.channels:
        webhook = await chany.create_webhook(name={userp})
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
            for i in range(1):
              await webhook.send(sned)

@roover.command(name="Rspam", description="Spams roles in a server")
@commands.cooldown(1, 13)
async def rspam(ctx, *, nam):
  await ctx.message.delete()
  for i in range(25):
        await ctx.guild.create_role(name=nam)

global lag_chat
lag_chat = [
        "🤰 🤱 👩‍🍼 🧑‍🍼 👨‍🍼 🙇‍♀️ 🙇 🙇‍♂️ 💁‍♀️ 💁 💁‍♂️ 🙅‍♀️ 🙅 🙅‍♂️ 🙆‍♀️ 🙆 🙆‍♂️ 🙋‍♀️ 🙋 🙋‍♂️ 🧏‍♀️ 🧏 🧏‍♂️ 🤦‍♀️ 🤦 🤦‍♂️ 🤷‍♀️ 🤷 🤷‍♂️ 🙎‍♀️ 🙎 🙎‍♂️ 🙍‍♀️ 🙍 🙍‍♂️ 💇‍♀️ 💇 💇‍♂️ 💆‍♀️ 💆 💆‍♂️ 🧖‍♀️ 🧖 🧖‍♂️ 💅 🤳 💃 🕺 👯‍♀️ 👯 👯‍♂️ 🕴 👩‍🦽 🧑‍🦽 👨‍🦽 👩‍🦼 🧑‍🦼 👨‍🦼 🚶‍♀️ 🚶 🚶‍♂️ 👩‍🦯 🧑‍🦯 👨‍🦯 🧎‍♀️ 🧎 🧎‍♂️ 🏃‍♀️ 🏃 🏃‍♂️ 🧍‍♀️ 🧍 🧍‍♂️ 👭 🧑‍🤝‍🧑 👬 👫 👩‍❤️‍👩 💑 👨‍❤️‍👨 👩‍❤️‍👨 👩‍❤️‍💋‍👩 💏 👨‍❤️‍💋‍👨 👩‍❤️‍💋‍👨 👪 👨‍👩‍👦 👨‍👩‍👧 👨‍👩‍👧‍👦 👨‍👩‍👦‍👦 👨‍👩‍👧‍👧 👨‍👨‍👦 👨‍👨‍👧 👨‍👨‍👧‍👦 👨‍👨‍👦‍👦 👨‍👨‍👧‍👧 👩‍👩‍👦 👩‍👩‍👧 👩‍👩‍👧‍👦 👩‍👩‍👦‍👦",
        "😀 😃 😄 😁 😆 😅 😂 🤣 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾",
        "👋 🤚 🖐 ✋ 🖖 👌 🤏 ✌️ 🤞 🤟 🤘 🤙 👈 👉 👆 🖕 👇 ☝️ 👍 👎 ✊ 👊 🤛 🤜 👏 🙌 👐 🤲 🤝 🙏 ✍️ 💅 🤳 💪 🦾 🦵 🦿 🦶 👂 🦻 👃 🧠 🦷 🦴 👀 👁 👅 👄 💋 🩸",
        "👶 🧒 👦 👧 🧑 👱 👨 🧔 👨‍🦰 👨‍🦱 👨‍🦳 👨‍🦲 👩 👩‍🦰 🧑‍🦰 👩‍🦱 🧑‍🦱 👩‍🦳 🧑‍🦳 👩‍🦲 🧑‍🦲 👱‍♀️ 👱‍♂️ 🧓 👴 👵 🙍 🙍‍♂️ 🙍‍♀️ 🙎 🙎‍♂️ 🙎‍♀️ 🙅 🙅‍♂️ 🙅‍♀️ 🙆 🙆‍♂️ 🙆‍♀️ 💁 💁‍♂️ 💁‍♀️ 🙋 🙋‍♂️ 🙋‍♀️ 🧏 🧏‍♂️ 🧏‍♀️ 🙇 🙇‍♂️ 🙇‍♀️ 🤦 🤦‍♂️ 🤦‍♀️ 🤷 🤷‍♂️ 🤷‍♀️ 🧑‍⚕️ 👨‍⚕️ 👩‍⚕️ 🧑‍🎓 👨‍🎓 👩‍🎓 🧑‍🏫 👨‍🏫 👩‍🏫 🧑‍⚖️ 👨‍⚖️ 👩‍⚖️ 🧑‍🌾 👨‍🌾 👩‍🌾 🧑‍🍳 👨‍🍳 👩‍🍳 🧑‍🔧 👨‍🔧 👩‍🔧 🧑‍🏭 👨‍🏭 👩‍🏭 🧑‍💼 👨‍💼 👩‍💼 🧑‍🔬 👨‍🔬 👩‍🔬 🧑‍💻 👨‍💻 👩‍💻 🧑‍🎤 👨‍🎤 👩‍🎤 🧑‍🎨 👨‍🎨 👩‍🎨 🧑‍✈️ 👨‍✈️ 👩‍✈️ 🧑‍🚀 👨‍🚀 👩‍🚀 🧑‍🚒 👨‍🚒 👩‍🚒 👮 👮‍♂️ 👮‍♀️ 🕵 🕵️‍♂️ 🕵️‍♀️ 💂 💂‍♂️ 💂‍♀️ 👷 👷‍♂️ 👷‍♀️ 🤴 👸 👳 👳‍♂️ 👳‍♀️ 👲 🧕 🤵 👰 🤰 🤱 👼 🎅 🤶 🦸 🦸‍♂️ 🦸‍♀️ 🦹 🦹‍♂️ 🦹‍♀️ 🧙 🧙‍♂️ 🧙‍♀️ 🧚 🧚‍♂️ 🧚‍♀️ 🧛 🧛‍♂️ 🧛‍♀️ 🧜 🧜‍♂️ 🧜‍♀️ 🧝 🧝‍♂️ 🧝‍♀️ 🧞 🧞‍♂️ 🧞‍♀️ 🧟 🧟‍♂️ 🧟‍♀️ 💆 💆‍♂️ 💆‍♀️ 💇 💇‍♂️ 💇‍♀️ 🚶 🚶‍♂️ 🚶‍♀️ 🧍 🧍‍♂️ 🧍‍♀️ 🧎 🧎‍♂️ 🧎‍♀️ 🧑‍🦯 👨‍🦯 👩‍🦯 🧑‍🦼 👨‍🦼 👩‍🦼 🧑‍🦽 👨‍🦽 👩‍🦽 🏃 🏃‍♂️ 🏃‍♀️ 💃 🕺 🕴 👯 👯‍♂️ 👯‍♀️ 🧖 🧖‍♂️ 🧖‍♀️ 🧘 🧑‍🤝‍🧑 👭 👫 👬 💏 👨‍❤️‍💋‍👨 👩‍❤️‍💋‍👩 💑 👨‍❤️‍👨 👩‍❤️‍👩 👪 👨‍👩‍👦 👨‍👩‍👧 👨‍👩‍👧‍👦 👨‍👩‍👦‍👦 👨‍👩‍👧‍👧 👨‍👨‍👦 👨‍👨‍👧 👨‍👨‍👧‍👦 👨‍👨‍👦‍👦 👨‍👨‍👧‍👧 👩‍👩‍👦 👩‍👩‍👧 👩‍👩‍👧‍👦 👩‍👩‍👦‍👦 👩‍👩‍👧‍👧 👨‍👦 👨‍👦‍👦 👨‍👧 👨‍👧‍👦 👨‍👧‍👧 👩‍👦 👩‍👦‍👦 👩‍👧 👩‍👧‍👦 👩‍👧‍👧 🗣 👤 👥 👣",
        "🧳 🌂 ☂️ 🧵 🧶 👓 🕶 🥽 🥼 🦺 👔 👕 👖 🧣 🧤 🧥 🧦 👗 👘 🥻 🩱 🩲 🩳 👙 👚 👛 👜 👝 🎒 👞 👟 🥾 👨🏻‍🚀 👩🏻‍🚀 🧑🏻‍🚒 👨🏻‍🚒 👩🏻‍🚒 👮🏻 👮🏻‍♂️ 👮🏻‍♀️ 🕵🏻 🕵🏻‍♂️ 🕵🏻‍♀️ 💂🏻 💂🏻‍♂️ 💂🏻‍♀️ 👷🏻 👷🏻‍♂️ 👷🏻‍♀️ 🤴🏻 👸🏻 👳🏻 👳🏻‍♂️ 👳🏻‍♀️ 👲🏻 🧕🏻 🤵🏻 👰🏻 🤰🏻 🤱🏻 👼🏻 🎅🏻 🤶🏻 🦸🏻 🦸🏻‍♂️ 🦸🏻‍♀️ 🦹🏻 🦹🏻‍♂️ 🦹🏻‍♀️ 🧙🏻 🧙🏻‍♂️ 🧙🏻‍♀️ 🧚🏻 🧚🏻‍♂️ 🧚🏻‍♀️ 🧛🏻 🧛🏻‍♂️ 🧛🏻‍♀️ 🧜🏻 🧜🏻‍♂️ 🧜🏻‍♀️ 🧝🏻 🧝🏻‍♂️ 🧝🏻‍♀️ 💆🏻 💆🏻‍♂️ 💆🏻‍♀️ 💇🏻 💇🏻‍♂️ 💇🏻‍♀️ 🚶🏻 🚶🏻‍♂️ 🚶🏻‍♀️ 🧍🏻 🧍🏻‍♂️ 🧍🏻‍♀️ 🧎🏻 🧎🏻‍♂️ 🧎🏻‍♀️ 🧑🏻‍🦯 👨🏻‍🦯 👩🏻‍🦯 🧑🏻‍🦼 👨🏻‍🦼 👩🏻‍🦼 🧑🏻‍🦽 👨🏻‍🦽 👩🏻‍🦽 🏃🏻 🏃🏻‍♂️ 🏃🏻‍♀️ 💃🏻 🕺🏻 🕴🏻 🧖🏻 🧖🏻‍♂️ 🧖🏻‍♀️ 🧗🏻 🧗🏻‍♂️ 🧗🏻‍♀️ 🏇🏻 🏂🏻 🏌🏻 🏌🏻‍♂️ 🏌🏻‍♀️ 🏄🏻 🏄🏻‍♂️ 🏄🏻‍♀️ 🚣🏻 🚣🏻‍♂️ 🚣🏻‍♀️ 🏊🏻 🏊🏻‍♂️ 🏊🏻‍♀️ ⛹🏻 ⛹🏻‍♂️ ⛹🏻‍♀️ 🏋🏻 🏋🏻‍♂️ 🏋🏻‍♀️ 🚴🏻 🚴🏻‍♂️ 🚴🏻‍♀️ 🚵🏻 🚵🏻‍♂️ 🚵🏻‍♀️ 🤸🏻 🤸🏻‍♂️ 🤸🏻‍♀️ 🤽🏻 🤽🏻‍♂️ 🤽🏻‍♀️ 🤾🏻 🤾🏻‍♂️ 🤾🏻‍♀️ 🤹🏻 🤹🏻‍♂️ 🤹🏻‍♀️ 🧘🏻 🧘🏻‍♂️ 🧘🏻‍♀️ 🛀🏻 🛌🏻 🧑🏻‍🤝‍🧑🏻 👬🏻 👭🏻 👫🏻",
        "👋🏽 🤚🏽 🖐🏽 ✋🏽 🖖🏽 👌🏽 🤏🏽 ✌🏽 🤞🏽 🤟🏽 🤘🏽 🤙🏽 👈🏽 👉🏽 👆🏽 🖕🏽 👇🏽 ☝🏽 👍🏽 👎🏽 ✊🏽 👊🏽 🤛🏽 🤜🏽 👏🏽 🙌🏽 👐🏽 🤲🏽 🙏🏽 ✍🏽 💅🏽 🤳🏽 💪🏽 🦵🏽 🦶🏽 👂🏽 🦻🏽 👃🏽 👶🏽 🧒🏽 👦🏽 👧🏽 🧑🏽 👨🏽 👩🏽 🧑🏽‍ 👨🏽‍🦱 👩🏽‍🦱 🧑🏽‍ 👨🏽‍🦰 👩🏽‍🦰 👱🏽 👱🏽‍♂️ 👱🏽‍♀️ 🧑🏽‍ 👨🏽‍🦳 👩🏽‍🦳 🧑🏽‍ 👨🏽‍🦲 👩🏽‍🦲 🧔🏽 🧓🏽 👴🏽 👵🏽 🙍🏽 🙍🏽‍♂️ 🙍🏽‍♀️ 🙎🏽 🙎🏽‍♂️ 🙎🏽‍♀️ 🙅🏽 🙅🏽‍♂️ 🙅🏽‍♀️ 🙆🏽 🙆🏽‍♂️ 🙆🏽‍♀️ 💁🏽 💁🏽‍♂️ 💁🏽‍♀️ 🙋🏽 🙋🏽‍♂️ 🙋🏽‍♀️ 🧏🏽 🧏🏽‍♂️ 🧏🏽‍♀️ 🙇🏽 🙇🏽‍♂️ 🙇🏽‍♀️ 🤦🏽 🤦🏽‍♂️ 🤦🏽‍♀️ 🤷🏽 🤷🏽‍♂️ 🤷🏽‍♀️ 🧑🏽‍⚕️ 👨🏽‍⚕️ 👩🏽‍⚕️ 🧑🏽‍🎓 👨🏽‍🎓 👩🏽‍🎓 🧑🏽‍🏫 👨🏽‍🏫 👩🏽‍🏫 🧑🏽‍⚖️ 👨🏽‍⚖️ 👩🏽‍⚖️ 🧑🏽‍🌾 👨🏽‍🌾 👩🏽‍🌾 🧑🏽‍🍳 👨🏽‍🍳 👩🏽‍🍳 🧑🏽‍🔧 👨🏽‍🔧 👩🏽‍🔧 🧑🏽‍🏭 👨🏽‍🏭 👩🏽‍🏭 🧑🏽‍💼 👨🏽‍💼 👩🏽‍💼 🧑🏽‍🔬 👨🏽‍🔬 👩🏽‍🔬 🧑🏽‍💻 👨🏽‍💻 👩🏽‍💻 🧑🏽‍🎤 👨🏽‍🎤 👩🏽‍🎤 🧑🏽‍🎨 👨🏽‍🎨 👩🏽‍🎨 🧑🏽‍✈️ 👨🏽‍✈️ 👩🏽‍✈️ 🧑🏽‍🚀 👨🏽‍🚀 👩🏽‍🚀 🧑🏽‍🚒 👨🏽‍🚒 👩🏽‍🚒 👮🏽 👮🏽‍♂️ 👮🏽‍♀️ 🕵🏽 🕵🏽‍♂️ 🕵🏽‍♀️ 💂🏽 💂🏽‍♂️ 💂🏽‍♀️ 👷🏽 👷🏽‍♂️ 👷🏽‍♀️ 🤴🏽 👸🏽 👳🏽 👳🏽‍♂️ 👳🏽‍♀️ 👲🏽 🧕🏽 🤵🏽 👰🏽 🤰🏽 🤱🏽 👼🏽 🎅🏽 🤶🏽 🦸🏽 🦸🏽‍♂️ 🦸🏽‍♀️ 🦹🏽 🦹🏽‍♂️ 🦹🏽‍♀️ 🧙🏽 🧙🏽‍♂️ 🧙🏽‍♀️ 🧚🏽 🧚🏽‍♂️ 🧚🏽‍♀️ 🧛🏽 🧛🏽‍♂️ 🧛🏽‍♀️ 🧜🏽 🧜🏽‍♂️ 🧜🏽‍♀️ 🧝🏽 🧝🏽‍♂️ 🧝🏽‍♀️ 💆🏽 💆🏽‍♂️ 💆🏽‍♀️ 💇🏽 💇🏽‍♂️ 💇🏽‍♀️ 🚶🏽 🚶🏽‍♂️ 🚶🏽‍♀️ 🧍🏽 🧍🏽‍♂️ 🧍🏽‍♀️ 🧎🏽 🧎🏽‍♂️ 🧎🏽‍♀️ 🧑🏽‍🦯 👨🏽‍🦯 👩🏽‍🦯 🧑🏽‍🦼 👨🏽‍🦼 👩🏽‍🦼 🧑🏽‍🦽 👨🏽‍🦽 👩🏽‍🦽 🏃🏽 🏃🏽‍♂️ 🏃🏽‍♀️ 💃🏽 🕺🏽 🕴🏽 🧖🏽 🧖🏽‍♂️ 🧖🏽‍♀️ 🧗🏽 🧗🏽‍♂️ 🧗🏽‍♀️ 🏇🏽 🏂🏽 🏌🏽 🏌🏽‍♂️ 🏌🏽‍♀️ 🏄🏽 🏄🏽‍♂️ 🏄🏽‍♀️ 🚣🏽 🚣🏽‍♂️ 🚣🏽‍♀️ 🏊🏽 🏊🏽‍♂️ 🏊🏽‍♀️ ⛹🏽 ⛹🏽‍♂️ ⛹🏽‍♀️ 🏋🏽 🏋🏽‍♂️ 🏋🏽‍♀️ 🚴🏽 🚴🏽‍♂️ 🚴🏽‍♀️ 🚵🏽 🚵🏽‍♂️ 🚵🏽‍♀️ 🤸🏽 🤸🏽‍♂️ 🤸🏽‍♀️ 🤽🏽 🤽🏽‍♂️ 🤽🏽‍♀️ 🤾🏽 🤾🏽‍♂️ 🤾🏽‍♀️ 🤹🏽 🤹🏽‍♂️ 🤹🏽‍♀️ 🧘🏽 🧘🏽‍♂️ 🧘🏽‍♀️ 🛀🏽 🛌🏽 🧑🏽‍🤝‍🧑🏽 👬🏽 👭🏽 👫🏽",
        "🐶 🐱 🐭 🐹 🐰 🦊 🐻 🐼 🐨 🐯 🦁 🐮 🐷 🐽 🐸 🐵 🙈 🙉 🙊 🐒 🐔 🐧 🐦 🐤 🐣 🐥 🦆 🦅 🦉 🦇 🐺 🐗 🐴 🦄 🐝 🐛 🦋 🐌 🐞 🐜 🦟 🦗 🕷 🕸 🦂 🐢 🐍 🦎 🦖 🦕 🐙 🦑 🦐 🦞 🦀 🐡 🐠 🐟 🐬 🐳 🐋 🦈 🐊 🐅 🐆 🦓 🦍 🦧 🐘 🦛 🦏 🐪 🐫 🦒 🦘 🐃 🐂 🐄 🐎 🐖 🐏 🐑 🦙 🐐 🦌 🐕 🐩 🦮 🐕‍🦺 🐈 🐓 🦃 🦚 🦜 🦢 🦩 🕊 🐇 🦝 🦨 🦡 🦦 🦥 🐁 🐀 🐿 🦔 🐾 🐉 🐲 🌵 🎄 🌲 🌳 🌴 🌱 🌿 ☘️ 🍀 🎍 🎋 🍃 🍂 🍁 🍄 🐚 🌾 💐 🌷 🌹 🥀 🌺 🌸 🌼 🌻 🌞 🌝 🌛 🌜 🌚 🌕 🌖 🌗 🌘 🌑 🌒 🌓 🌔 🌙 🌎 🌍 🌏 🪐 💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥 🌪 🌈 ☀️ 🌤 ⛅️ 🌥 ☁️ 🌦 🌧 ⛈ 🌩 🌨 ❄️ ☃️ ⛄️ 🌬 💨 💧 💦 ☔️ ☂️ 🌊 🌫",
        "🍏 🍎 🍐 🍊 🍋 🍌 🍉 🍇 🍓 🍈 🍒 🍑 🥭 🍍 🥥 🥝 🍅 🍆 🥑 🥦 🥬 🥒 🌶 🌽 🥕 🧄 🧅 🥔 🍠 🥐 🥯 🍞 🥖 🥨 🧀 🥚 🍳 🧈 🥞 🧇 🥓 🥩 🍗 🍖 🦴 🌭 🍔 🍟 🍕 🥪 🥙 🧆 🌮 🌯 🥗 🥘 🥫 🍝 🍜 🍲 🍛 🍣 🍱 🥟 🦪 🍤 🍙 🍚 🍘 🍥 🥠 🥮 🍢 🍡 🍧 🍨 🍦 🥧 🧁 🍰 🎂 🍮 🍭 🍬 🍫 🍿 🍩 🍪 🌰 🥜 🍯 🥛 🍼 ☕️ 🍵 🧃 🥤 🍶 🍺 🍻 🥂 🍷 🥃 🍸 🍹 🧉 🍾 🧊 🥄 🍴 🍽 🥣 🥡 🥢 🧂",
        "⚽️ 🏀 🏈 ⚾️ 🥎 🎾 🏐 🏉 🥏 🎱 🪀 🏓 🏸 🏒 🏑 🥍 🏏 🥅 ⛳️ 🪁 🏹 🎣 🤿 🥊 🥋 🎽 🛹 🛷 ⛸ 🥌 🎿 ⛷ 🏂 🪂 🏋️ 🏋️‍♂️ 🏋️‍♀️ 🤼 🤼‍♂️ 🤼‍♀️ 🤸‍♀️ 🤸 🤸‍♂️ ⛹️ ⛹️‍♂️ ⛹️‍♀️ 🤺 🤾 🤾‍♂️ 🤾‍♀️ 🏌️ 🏌️‍♂️ 🏌️‍♀️ 🏇 🧘 🧘‍♂️ 🧘‍♀️ 🏄 🏄‍♂️ 🏄‍♀️ 🏊 🏊‍♂️ 🏊‍♀️ 🤽 🤽‍♂️ 🤽‍♀️ 🚣 🚣‍♂️ 🚣‍♀️ 🧗 🧗‍♂️ 🧗‍♀️ 🚵 🚵‍♂️ 🚵‍♀️ 🚴 🚴‍♂️ 🚴‍♀️ 🏆 🥇 🥈 🥉 🏅 🎖 🏵 🎗 🎫 🎟 🎪 🤹 🤹‍♂️ 🤹‍♀️ 🎭 🩰 🎨 🎬 🎤 🎧 🎼 🎹 🥁 🎷 🎺 🎸 🪕 🎻 🎲 ♟ 🎯 🎳 🎮 🎰 🧩",
        "⚽️ 🏀 🏈 ⚾️ 🥎 🎾 🏐 🏉 🥏 🎱 🪀 🏓 🏸 🏒 🏑 🥍 🏏 🥅 ⛳️ 🪁 🏹 🎣 🤿 🥊 🥋 🎽 🛹 🛷 ⛸ 🥌 🎿 ⛷ 🏂 🪂 🏋️ 🏋️‍♂️ 🏋️‍♀️ 🤼 🤼‍♂️ 🤼‍♀️ 🤸‍♀️ 🤸 🤸‍♂️ ⛹️ ⛹️‍♂️ ⛹️‍♀️ 🤺 🤾 🤾‍♂️ 🤾‍♀️ 🏌️ 🏌️‍♂️ 🏌️‍♀️ 🏇 🧘 🧘‍♂️ 🧘‍♀️ 🏄 🏄‍♂️ 🏄‍♀️ 🏊 🏊‍♂️ 🏊‍♀️ 🤽 🤽‍♂️ 🤽‍♀️ 🚣 🚣‍♂️ 🚣‍♀️ 🧗 🧗‍♂️ 🧗‍♀️ 🚵 🚵‍♂️ 🚵‍♀️ 🚴 🚴‍♂️ 🚴‍♀️ 🏆 🥇 🥈 🥉 🏅 🎖 🏵 🎗 🎫 🎟 🎪 🤹 🤹‍♂️ 🤹‍♀️ 🎭 🩰 🎨 🎬 🎤 🎧 🎼 🎹 🥁 🎷 🎺 🎸 🪕 🎻 🎲 ♟ 🎯 🎳 🎮 🎰 🧩",
        "🚗 🚕 🚙 🚌 🚎 🏎 🚓 🚑 🚒 🚐 🚚 🚛 🚜 🦯 🦽 🦼 🛴 🚲 🛵 🏍 🛺 🚨 🚔 🚍 🚘 🚖 🚡 🚠 🚟 🚃 🚋 🚞 🚝 🚄 🚅 🚈 🚂 🚆 🚇 🚊 🚉 ✈️ 🛫 🛬 🛩 💺 🛰 🚀 🛸 🚁 🛶 ⛵️ 🚤 🛥 🛳 ⛴ 🚢 ⚓️ ⛽️ 🚧 🚦 🚥 🚏 🗺 🗿 🗽 🗼 🏰 🏯 🏟 🎡 🎢 🎠 ⛲️ ⛱ 🏖 🏝 🏜 🌋 ⛰ 🏔 🗻 🏕 ⛺️ 🏠 🏡 🏘 🏚 🏗 🏭 🏢 🏬 🏣 🏤 🏥 🏦 🏨 🏪 🏫 🏩 💒 🏛 ⛪️ 🕌 🕍 🛕 🕋 ⛩ 🛤 🛣 🗾 🎑 🏞 🌅 🌄 🌠 🎇 🎆 🌇 🌆 🏙 🌃 🌌 🌉 🌁",
        "⌚️ 📱 📲 💻 ⌨️ 🖥 🖨 🖱 🖲 🕹 🗜 💽 💾 💿 📀 📼 📷 📸 📹 🎥 📽 🎞 📞 ☎️ 📟 📠 📺 📻 🎙 🎚 🎛 🧭 ⏱ ⏲ ⏰ 🕰 ⌛️ ⏳ 📡 🔋 🔌 💡 🔦 🕯 🪔 🧯 🛢 💸 💵 💴 💶 💷 💰 💳 💎 ⚖️ 🧰 🔧 🔨 ⚒ 🛠 ⛏ 🔩 ⚙️ 🧱 ⛓ 🧲 🔫 💣 🧨 🪓 🔪 🗡 ⚔️ 🛡 🚬 ⚰️ ⚱️ 🏺 🔮 📿 🧿 💈 ⚗️ 🔭 🔬 🕳 🩹 🩺 💊 💉 🩸 🧬 🦠 🧫 🧪 🌡 🧹 🧺 🧻 🚽 🚰 🚿 🛁 🛀 🧼 🛌 🧸 🖼 🛍 🛒 🎁 🎈 🎏 🎀🕣 🕤 🕥 🕦 🕧",
        "😀 😃 😄 😁 😆 😅 😂 🤣 🥲 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🥸 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾",
        "👨‍⚖️ 👰‍♀️ 👰 👰‍♂️ 🤵‍♀️ 🤵 🤵‍♂️ 👸 🤴 🥷 🦸‍♀️ 🦸 🦸‍♂️ 🦹‍♀️ 🦹 🦹‍♂️ 🤶 🧑‍🎄 🎅 🧙‍♀️ 🧙 🧙‍♂️ 🧝‍♀️ 🧝 🧝‍♂️ 🧛‍♀️ 🧛 🧛‍♂️ 🧟‍♀️ 🧟 🧟‍♂️ 🧞‍♀️ 🧞 🧞‍♂️ 🧜‍♀️ 🧜 🧜‍♂️ 🧚‍♀️ 🧚 🧚‍♂️ 👼 🤰 🤱 👩‍🍼 🧑‍🍼 👨‍🍼 🙇‍♀️ 🙇 🙇‍♂️ 💁‍♀️ 💁 💁‍♂️ 🙅‍♀️ 🙅 🙅‍♂️ 🙆‍♀️ 🙆 🙆‍♂️ 🙋‍♀️ 🙋 🙋‍♂️ 🧏‍♀️ 🧏 🧏‍♂️ 🤦‍♀️ 🤦 🤦‍♂️ 🤷‍♀️ 🤷 🤷‍♂️ 🙎‍♀️ 🙎 🙎‍♂️ 🙍‍♀️ 🙍 🙍‍♂️ 💇‍♀️ 💇 💇‍♂️ 💆‍♀️ 💆 💆‍♂️ 🧖‍♀️ 🧖 🧖‍♂️",
        " 🧖‍♂️ 💅 🤳 💃 🕺 👯‍♀️ 👯 👯‍♂️ 🕴 👩‍🦽 🧑‍🦽 👨‍🦽 👩‍🦼 🧑‍🦼 👨‍🦼 🚶‍♀️ 🚶 🚶‍♂️ 👩‍🦯 🧑‍🦯 👨‍🦯 🧎‍♀️ 🧎 🧎‍♂️ 🏃‍♀️ 🏃 🏃‍♂️ 🧍‍♀️ 🧍 🧍‍♂️ 👭 🧑‍🤝‍🧑 👬 👫 👩‍❤️‍👩 💑 👨‍❤️‍👨 👩‍❤️‍👨 👩‍❤️‍💋‍👩 💏 👨‍❤️‍💋‍👨 👩‍❤️‍💋‍👨 👪 👨‍👩‍👦 👨‍👩‍👧 👨‍👩‍👧‍👦 👨‍👩‍👦‍👦 👨‍👩‍👧‍👧 👨‍👨‍👦 👨‍👨‍👧 👨‍👨‍👧‍👦 👨‍👨‍👦‍👦 👨‍👨‍👧‍👧 👩‍👩‍👦 👩‍👩‍👧 👩‍👩‍👧‍👦 👩‍👩‍👦‍👦 👩‍👩‍👧‍👧 👨‍👦 👨‍👦‍👦 👨‍👧 👨‍👧‍👦 👨‍👧‍👧 👩‍👦 👩‍👦‍👦 👩‍👧 👩‍👧‍👦 👩‍👧‍👧 🗣 👤 👥 🫂",
        "🧜 🧜‍♂️ 🧚‍♀️ 🧚 🧚‍♂️ 👼 🤰 🤱 👩‍🍼 🧑‍🍼 👨‍🍼 🙇‍♀️ 🙇 🙇‍♂️ 💁‍♀️ 💁 💁‍♂️ 🙅‍♀️ 🙅 🙅‍♂️ 🙆‍♀️ 🙆 🙆‍♂️ 🙋‍♀️ 🙋 🙋‍♂️ 🧏‍♀️ 🧏 🧏‍♂️ 🤦‍♀️ 🤦 🤦‍♂️ 🤷‍♀️ 🤷 🤷‍♂️ 🙎‍♀️ 🙎 🙎‍♂️ 🙍‍♀️ 🙍 🙍‍♂️ 💇‍♀️ 💇 💇‍♂️ 💆‍♀️ 💆 💆‍♂️ 🧖‍♀️ 🧖 🧖‍♂️ 💅 🤳 💃 🕺 👯‍♀️ 👯 👯‍♂️ 🕴 👩‍🦽 🧑‍🦽 👨‍🦽 👩‍🦼 🧑‍🦼 👨‍🦼 🚶‍♀️ 🚶 🚶‍♂️ 👩‍🦯 🧑‍🦯 👨‍🦯 🧎‍♀️ 🧎 🧎‍♂️ 🏃‍♀️ 🏃 🏃‍♂️ 🧍‍♀️ 🧍 🧍‍♂️ 👭 🧑‍🤝‍🧑 👬 👫 👩‍❤️‍👩 💑 👨‍❤️‍👨 👩‍❤️‍👨 👩‍❤️‍💋‍👩 💏 👨‍❤️‍💋‍👨 👩‍❤️‍💋‍👨 👪 👨‍👩‍👦 👨‍👩‍👧 👨‍👩‍👧‍👦 👨‍👩‍👦‍👦 👨‍👩‍👧‍👧 👨‍👨‍👦 👨‍👨‍👧 👨‍👨‍👧‍👦 👨‍👨‍👦‍👦 👨‍👨‍👧‍👧 👩‍👩‍👦 👩‍👩‍👧 👩‍👩‍👧‍👦 👩‍👩‍👦‍👦 👩‍👩‍👧‍👧 👨‍👦 👨‍👦‍👦 👨‍👧 👨‍👧‍👦 👨‍👧‍👧 👩‍👦 👩‍👦‍👦 👩‍👧 👩‍👧‍👦 👩‍👧‍👧 🗣 👤 👥 🫂",
        "🧳 🌂 ☂️ 🧵 🪡 🪢 🧶 👓 🕶 🥽 🥼 🦺 👔 👕 👖 🧣 🧤 🧥 🧦 👗 👘 🥻 🩴 🩱 🩲 🩳 👙 👚 👛 👜 👝 🎒 👞 👟 🥾 🥿 👠 👡 🩰 👢 👑 👒 🎩 🎓 🧢 ⛑ 🪖 💄 💍 💼👋🏻 🤚🏻 🖐🏻 ✋🏻 🖖🏻 👌🏻 🤌🏻 🤏🏻 ✌🏻 🤞🏻 🤟🏻 🤘🏻 🤙🏻 👈🏻 👉🏻 👆🏻 🖕🏻 👇🏻 ☝🏻 👍🏻 👎🏻 ✊🏻 👊🏻 🤛🏻 🤜🏻 👏🏻 🙌🏻 👐🏻 🤲🏻 🙏🏻 ✍🏻 💅🏻 🤳🏻 💪🏻 🦵🏻 🦶🏻 👂🏻 🦻🏻 👃🏻 👶🏻 👧🏻 🧒🏻 👦🏻 👩🏻 🧑🏻 👨🏻 👩🏻‍🦱 🧑🏻‍🦱 👨🏻‍🦱",
        "👩🏻‍🦱 🧑🏻‍🦱 👨🏻‍🦱 👩🏻‍🦰 🧑🏻‍🦰 👨🏻‍🦰 👱🏻‍♀️ 👱🏻 👱🏻‍♂️ 👩🏻‍🦳 🧑🏻‍🦳 👨🏻‍🦳 👩🏻‍🦲 🧑🏻‍🦲 👨🏻‍🦲 🧔🏻 👵🏻 🧓🏻 👴🏻 👲🏻 👳🏻‍♀️ 👳🏻 👳🏻‍♂️ 🧕🏻 👮🏻‍♀️ 👮🏻 👮🏻‍♂️ 👷🏻‍♀️ 👷🏻 👷🏻‍♂️ 💂🏻‍♀️ 💂🏻 💂🏻‍♂️ 🕵🏻‍♀️ 🕵🏻 🕵🏻‍♂️ 👩🏻‍⚕️ 🧑🏻‍⚕️ 👨🏻‍⚕️ 👩🏻‍🌾 🧑🏻‍🌾 👨🏻‍🌾 👩🏻‍🍳 🧑🏻‍🍳 👨🏻‍🍳 👩🏻‍🎓 🧑🏻‍🎓 👨🏻‍🎓 👩🏻‍🎤 🧑🏻‍🎤 👨🏻‍🎤 👩🏻‍🏫 🧑🏻‍🏫 👨🏻‍🏫 👩🏻‍🏭 🧑🏻‍🏭 👨🏻‍🏭 👩🏻‍💻 🧑🏻‍💻 👨🏻‍💻 👩🏻‍💼 🧑🏻‍💼 👨🏻‍💼 👩🏻‍🔧 🧑🏻‍🔧 👨🏻‍🔧 👩🏻‍🔬 🧑🏻‍🔬 👨🏻‍🔬 👩🏻‍🎨 🧑🏻‍🎨 👨🏻‍🎨 👩🏻‍🚒 🧑🏻‍🚒 👨🏻‍🚒 👩🏻‍✈️ 🧑🏻‍✈️ 👨🏻‍✈️ 👩🏻‍🚀 🧑🏻‍🚀 👨🏻‍🚀 👩🏻‍⚖️",
        "🧑🏻‍🚒 👨🏻‍🚒 👩🏻‍✈️ 🧑🏻‍✈️ 👨🏻‍✈️ 👩🏻‍🚀 🧑🏻‍🚀 👨🏻‍🚀 👩🏻‍⚖️ 🧑🏻‍⚖️ 👨🏻‍⚖️ 👰🏻‍♀️ 👰🏻 👰🏻‍♂️ 🤵🏻‍♀️ 🤵🏻 🤵🏻‍♂️ 👸🏻 🤴🏻 🥷🏻 🦸🏻‍♀️ 🦸🏻 🦸🏻‍♂️ 🦹🏻‍♀️ 🦹🏻 🦹🏻‍♂️ 🤶🏻 🧑🏻‍🎄 🎅🏻 🧙🏻‍♀️ 🧙🏻 🧙🏻‍♂️ 🧝🏻‍♀️ 🧝🏻 🧝🏻‍♂️ 🧛🏻‍♀️ 🧛🏻 🧛🏻‍♂️ 🧜🏻‍♀️ 🧜🏻 🧜🏻‍♂️ 🧚🏻‍♀️ 🧚🏻 🧚🏻‍♂️ 👼🏻 🤰🏻 🤱🏻 👩🏻‍🍼 🧑🏻‍🍼 👨🏻‍🍼 🙇🏻‍♀️ 🙇🏻 🙇🏻‍♂️ 💁🏻‍♀️ 💁🏻 💁🏻‍♂️ 🙅🏻‍♀️ 🙅🏻 🙅🏻‍♂️ 🙆🏻‍♀️ 🙆🏻 🙆🏻‍♂️ 🙋🏻‍♀️ 🙋🏻 🙋🏻‍♂️ 🧏🏻‍♀️ 🧏🏻 🧏🏻‍♂️ 🤦🏻‍♀️ 🤦🏻 🤦🏻‍♂️ 🤷🏻‍♀️ 🤷🏻 🤷🏻‍♂️ 🙎🏻‍♀️ 🙎🏻 🙎🏻‍♂️ 🙍🏻‍♀️ 🙍🏻 🙍🏻‍♂️ 💇🏻‍♀️ 💇🏻 💇🏻‍♂️ 💆🏻‍♀️ 💆🏻 💆🏻‍♂️ 🧖🏻‍♀️ 🧖🏻 🧖🏻‍♂️ 💃🏻 🕺🏻 🕴🏻 👩🏻‍🦽 🧑🏻‍🦽 👨🏻‍🦽 👩🏻‍🦼 🧑🏻‍🦼 👨🏻‍🦼 🚶🏻‍♀️ ",
        "🧑🏻‍🦼 👨🏻‍🦼 🚶🏻‍♀️ 🚶🏻 🚶🏻‍♂️ 👩🏻‍🦯 🧑🏻‍🦯 👨🏻‍🦯 🧎🏻‍♀️ 🧎🏻 🧎🏻‍♂️ 🏃🏻‍♀️ 🏃🏻 🏃🏻‍♂️ 🧍🏻‍♀️ 🧍🏻 🧍🏻‍♂️ 👭🏻 🧑🏻‍🤝‍🧑🏻 👬🏻 👫🏻 🧗🏻‍♀️ 🧗🏻 🧗🏻‍♂️ 🏇🏻 🏂🏻 🏌🏻‍♀️ 🏌🏻 🏌🏻‍♂️ 🏄🏻‍♀️ 🏄🏻 🏄🏻‍♂️ 🚣🏻‍♀️ 🚣🏻 🚣🏻‍♂️ 🏊🏻‍♀️ 🏊🏻 🏊🏻‍♂️ ⛹🏻‍♀️ ⛹🏻 ⛹🏻‍♂️ 🏋🏻‍♀️ 🏋🏻 🏋🏻‍♂️ 🚴🏻‍♀️ 🚴🏻 🚴🏻‍♂️ 🚵🏻‍♀️ 🚵🏻 🚵🏻‍♂️ 🤸🏻‍♀️ 🤸🏻 🤸🏻‍♂️ 🤽🏻‍♀️ 🤽🏻 🤽🏻‍♂️ 🤾🏻‍♀️ 🤾🏻 🤾🏻‍♂️ 🤹🏻‍♀️ 🤹🏻 🤹🏻‍♂️ 🧘🏻‍♀️ 🧘🏻 🧘🏻‍♂️ 🛀🏻 🛌🏻",
        "👋🏼 🤚🏼 🖐🏼 ✋🏼 🖖🏼 👌🏼 🤌🏼 🤏🏼 ✌🏼 🤞🏼 🤟🏼 🤘🏼 🤙🏼 👈🏼 👉🏼 👆🏼 🖕🏼 👇🏼 ☝🏼 👍🏼 👎🏼 ✊🏼 👊🏼 🤛🏼 🤜🏼 👏🏼 🙌🏼 👐🏼 🤲🏼 🙏🏼 ✍🏼 💅🏼 🤳🏼 💪🏼 🦵🏼 🦶🏼 👂🏼 🦻🏼 👃🏼 👶🏼 👧🏼 🧒🏼 👦🏼 👩🏼 🧑🏼 👨🏼 👩🏼‍🦱 🧑🏼‍🦱 👨🏼‍🦱 👩🏼‍🦰 🧑🏼‍🦰 👨🏼‍🦰 👱🏼‍♀️ 👱🏼 👱🏼‍♂️ 👩🏼‍🦳 🧑🏼‍🦳 👨🏼‍🦳 👩🏼‍🦲 🧑🏼‍🦲 👨🏼‍🦲 🧔🏼 👵🏼 🧓🏼 👴🏼 👲🏼 👳🏼‍♀️ 👳🏼 👳🏼‍♂️ 🧕🏼 👮🏼‍♀️ 👮🏼 👮🏼‍♂️ 👷🏼‍♀️ 👷🏼 👷🏼‍♂️ 💂🏼‍♀️ 💂🏼 💂🏼‍♂️ 🕵🏼‍♀️ 🕵🏼",
        "💂🏼 💂🏼‍♂️ 🕵🏼‍♀️ 🕵🏼 🕵🏼‍♂️ 👩🏼‍⚕️ 🧑🏼‍⚕️ 👨🏼‍⚕️ 👩🏼‍🌾 🧑🏼‍🌾 👨🏼‍🌾 👩🏼‍🍳 🧑🏼‍🍳 👨🏼‍🍳 👩🏼‍🎓 🧑🏼‍🎓 👨🏼‍🎓 👩🏼‍🎤 🧑🏼‍🎤 👨🏼‍🎤 👩🏼‍🏫 🧑🏼‍🏫 👨🏼‍🏫 👩🏼‍🏭 🧑🏼‍🏭 👨🏼‍🏭 👩🏼‍💻 🧑🏼‍💻 👨🏼‍💻 👩🏼‍💼 🧑🏼‍💼 👨🏼‍💼 👩🏼‍🔧 🧑🏼‍🔧 👨🏼‍🔧 👩🏼‍🔬 🧑🏼‍🔬 👨🏼‍🔬 👩🏼‍🎨 🧑🏼‍🎨 👨🏼‍🎨 👩🏼‍🚒 🧑🏼‍🚒 👨🏼‍🚒 👩🏼‍✈️ 🧑🏼‍✈️ 👨🏼‍✈️ 👩🏼‍🚀 🧑🏼‍🚀 👨🏼‍🚀 👩🏼‍⚖️ 🧑🏼‍⚖️ 👨🏼‍⚖️ 👰🏼‍♀️ 👰🏼 👰🏼‍♂️ 🤵🏼‍♀️ 🤵🏼 🤵🏼‍♂️ 👸🏼 🤴🏼 🥷🏼",
        " 🤵🏼‍♀️ 🤵🏼 🤵🏼‍♂️ 👸🏼 🤴🏼 🥷🏼 🦸🏼‍♀️ 🦸🏼 🦸🏼‍♂️ 🦹🏼‍♀️ 🦹🏼 🦹🏼‍♂️ 🤶🏼 🧑🏼‍🎄 🎅🏼 🧙🏼‍♀️ 🧙🏼 🧙🏼‍♂️ 🧝🏼‍♀️ 🧝🏼 🧝🏼‍♂️ 🧛🏼‍♀️ 🧛🏼 🧛🏼‍♂️ 🧜🏼‍♀️ 🧜🏼 🧜🏼‍♂️ 🧚🏼‍♀️ 🧚🏼 🧚🏼‍♂️ 👼🏼 🤰🏼 🤱🏼 👩🏼‍🍼 🧑🏼‍🍼 👨🏼‍🍼 🙇🏼‍♀️ 🙇🏼 🙇🏼‍♂️ 💁🏼‍♀️ 💁🏼 💁🏼‍♂️ 🙅🏼‍♀️ 🙅🏼 🙅🏼‍♂️ 🙆🏼‍♀️ 🙆🏼 🙆🏼‍♂️ 🙋🏼‍♀️ 🙋🏼 🙋🏼‍♂️ 🧏🏼‍♀️ 🧏🏼 🧏🏼‍♂️ 🤦🏼‍♀️ 🤦🏼 🤦🏼‍♂️ 🤷🏼‍♀️ 🤷🏼 🤷🏼‍♂️ 🙎🏼‍♀️ 🙎🏼 🙎🏼‍♂️ 🙍🏼‍♀️ 🙍🏼 🙍🏼‍♂️ 💇🏼‍♀️ 💇🏼 💇🏼‍♂️ 💆🏼‍♀️ 💆🏼 💆🏼‍♂️ 🧖🏼‍♀️ 🧖🏼 🧖🏼‍♂️ 💃🏼 🕺🏼 🕴🏼 👩🏼‍🦽 🧑🏼‍🦽 👨🏼‍🦽 👩🏼‍🦼 🧑🏼‍🦼 👨🏼‍🦼 ",
        " 👨🏼‍🦼 🚶🏼‍♀️ 🚶🏼 🚶🏼‍♂️ 👩🏼‍🦯 🧑🏼‍🦯 👨🏼‍🦯 🧎🏼‍♀️ 🧎🏼 🧎🏼‍♂️ 🏃🏼‍♀️ 🏃🏼 🏃🏼‍♂️ 🧍🏼‍♀️ 🧍🏼 🧍🏼‍♂️ 👭🏼 🧑🏼‍🤝‍🧑🏼 👬🏼 👫🏼 🧗🏼‍♀️ 🧗🏼 🧗🏼‍♂️ 🏇🏼 🏂🏼 🏌🏼‍♀️ 🏌🏼 🏌🏼‍♂️ 🏄🏼‍♀️ 🏄🏼 🏄🏼‍♂️ 🚣🏼‍♀️ 🚣🏼 🚣🏼‍♂️ 🏊🏼‍♀️ 🏊🏼 🏊🏼‍♂️ ⛹🏼‍♀️ ⛹🏼 ⛹🏼‍♂️ 🏋🏼‍♀️ 🏋🏼 🏋🏼‍♂️ 🚴🏼‍♀️ 🚴🏼 🚴🏼‍♂️ 🚵🏼‍♀️ 🚵🏼 🚵🏼‍♂️ 🤸🏼‍♀️ 🤸🏼 🤸🏼‍♂️ 🤽🏼‍♀️ 🤽🏼 🤽🏼‍♂️ 🤾🏼‍♀️ 🤾🏼 🤾🏼‍♂️ 🤹🏼‍♀️ 🤹🏼 🤹🏼‍♂️ 🧘🏼‍♀️ 🧘🏼 🧘🏼‍♂️ 🛀🏼 🛌🏼",
        "👋🏽 🤚🏽 🖐🏽 ✋🏽 🖖🏽 👌🏽 🤌🏽 🤏🏽 ✌🏽 🤞🏽 🤟🏽 🤘🏽 🤙🏽 👈🏽 👉🏽 👆🏽 🖕🏽 👇🏽 ☝🏽 👍🏽 👎🏽 ✊🏽 👊🏽 🤛🏽 🤜🏽 👏🏽 🙌🏽 👐🏽 🤲🏽 🙏🏽 ✍🏽 💅🏽 🤳🏽 💪🏽 🦵🏽 🦶🏽 👂🏽 🦻🏽 👃🏽 👶🏽 👧🏽 🧒🏽 👦🏽 👩🏽 🧑🏽 👨🏽 👩🏽‍🦱 🧑🏽‍🦱 👨🏽‍🦱 👩🏽‍🦰 🧑🏽‍🦰 👨🏽‍🦰 👱🏽‍♀️ 👱🏽 👱🏽‍♂️ 👩🏽‍🦳 🧑🏽‍🦳 👨🏽‍🦳 👩🏽‍🦲 🧑🏽‍🦲 👨🏽‍🦲 🧔🏽 👵🏽 🧓🏽 👴🏽 👲🏽 👳🏽‍♀️ 👳🏽 👳🏽‍♂️ 🧕🏽 👮🏽‍♀️ 👮🏽 👮🏽‍♂️ 👷🏽‍♀️ 👷🏽 👷🏽‍♂️ 💂🏽‍♀️ 💂🏽",
        "💂🏽‍♀️ 💂🏽 💂🏽‍♂️ 🕵🏽‍♀️ 🕵🏽 🕵🏽‍♂️ 👩🏽‍⚕️ 🧑🏽‍⚕️ 👨🏽‍⚕️ 👩🏽‍🌾 🧑🏽‍🌾 👨🏽‍🌾 👩🏽‍🍳 🧑🏽‍🍳 👨🏽‍🍳 👩🏽‍🎓 🧑🏽‍🎓 👨🏽‍🎓 👩🏽‍🎤 🧑🏽‍🎤 👨🏽‍🎤 👩🏽‍🏫 🧑🏽‍🏫 👨🏽‍🏫 👩🏽‍🏭 🧑🏽‍🏭 👨🏽‍🏭 👩🏽‍💻 🧑🏽‍💻 👨🏽‍💻 👩🏽‍💼 🧑🏽‍💼 👨🏽‍💼 👩🏽‍🔧 🧑🏽‍🔧 👨🏽‍🔧 👩🏽‍🔬 🧑🏽‍🔬 👨🏽‍🔬 👩🏽‍🎨 🧑🏽‍🎨 👨🏽‍🎨 👩🏽‍🚒 🧑🏽‍🚒 👨🏽‍🚒 👩🏽‍✈️ 🧑🏽‍✈️ 👨🏽‍✈️ 👩🏽‍🚀 🧑🏽‍🚀 👨🏽‍🚀 👩🏽‍⚖️ 🧑🏽‍⚖️ 👨🏽‍⚖️ 👰🏽‍♀️ 👰🏽 👰🏽‍♂️ 🤵🏽‍♀️ 🤵🏽 🤵🏽‍♂️ ",
        " 🤵🏽 🤵🏽‍♂️ 👸🏽 🤴🏽 🥷🏽 🦸🏽‍♀️ 🦸🏽 🦸🏽‍♂️ 🦹🏽‍♀️ 🦹🏽 🦹🏽‍♂️ 🤶🏽 🧑🏽‍🎄 🎅🏽 🧙🏽‍♀️ 🧙🏽 🧙🏽‍♂️ 🧝🏽‍♀️ 🧝🏽 🧝🏽‍♂️ 🧛🏽‍♀️ 🧛🏽 🧛🏽‍♂️ 🧜🏽‍♀️ 🧜🏽 🧜🏽‍♂️ 🧚🏽‍♀️ 🧚🏽 🧚🏽‍♂️ 👼🏽 🤰🏽 🤱🏽 👩🏽‍🍼 🧑🏽‍🍼 👨🏽‍🍼 🙇🏽‍♀️ 🙇🏽 🙇🏽‍♂️ 💁🏽‍♀️ 💁🏽 💁🏽‍♂️ 🙅🏽‍♀️ 🙅🏽 🙅🏽‍♂️ 🙆🏽‍♀️ 🙆🏽 🙆🏽‍♂️ 🙋🏽‍♀️ 🙋🏽 🙋🏽‍♂️ 🧏🏽‍♀️ 🧏🏽 🧏🏽‍♂️ 🤦🏽‍♀️ 🤦🏽 🤦🏽‍♂️ 🤷🏽‍♀️ 🤷🏽 🤷🏽‍♂️ 🙎🏽‍♀️ 🙎🏽 🙎🏽‍♂️ 🙍🏽‍♀️ 🙍🏽 🙍🏽‍♂️ 💇🏽‍♀️ 💇🏽 💇🏽‍♂️ 💆🏽‍♀️ 💆🏽 💆🏽‍♂️ 🧖🏽‍♀️ 🧖🏽 🧖🏽‍♂️ 💃🏽 🕺🏽 🕴🏽 👩🏽‍🦽 🧑🏽‍🦽 👨🏽‍🦽 👩🏽‍🦼 🧑🏽‍🦼 👨🏽‍🦼 🚶🏽‍♀️",
        " 👨🏽‍🦯 🧎🏽‍♀️ 🧎🏽 🧎🏽‍♂️ 🏃🏽‍♀️ 🏃🏽 🏃🏽‍♂️ 🧍🏽‍♀️ 🧍🏽 🧍🏽‍♂️ 👭🏽 🧑🏽‍🤝‍🧑🏽 👬🏽 👫🏽 🧗🏽‍♀️ 🧗🏽 🧗🏽‍♂️ 🏇🏽 🏂🏽 🏌🏽‍♀️ 🏌🏽 🏌🏽‍♂️ 🏄🏽‍♀️ 🏄🏽 🏄🏽‍♂️ 🚣🏽‍♀️ 🚣🏽 🚣🏽‍♂️ 🏊🏽‍♀️ 🏊🏽 🏊🏽‍♂️ ⛹🏽‍♀️ ⛹🏽 ⛹🏽‍♂️ 🏋🏽‍♀️ 🏋🏽 🏋🏽‍♂️ 🚴🏽‍♀️ 🚴🏽 🚴🏽‍♂️ 🚵🏽‍♀️ 🚵🏽 🚵🏽‍♂️ 🤸🏽‍♀️ 🤸🏽 🤸🏽‍♂️ 🤽🏽‍♀️ 🤽🏽 🤽🏽‍♂️ 🤾🏽‍♀️ 🤾🏽 🤾🏽‍♂️ 🤹🏽‍♀️ 🤹🏽 🤹🏽‍♂️ 🧘🏽‍♀️ 🧘🏽 🧘🏽‍♂️ 🛀🏽 🛌🏽",
        "👋🏾 🤚🏾 🖐🏾 ✋🏾 🖖🏾 👌🏾 🤌🏾 🤏🏾 ✌🏾 🤞🏾 🤟🏾 🤘🏾 🤙🏾 👈🏾 👉🏾 👆🏾 🖕🏾 👇🏾 ☝🏾 👍🏾 👎🏾 ✊🏾 👊🏾 🤛🏾 🤜🏾 👏🏾 🙌🏾 👐🏾 🤲🏾 🙏🏾 ✍🏾 💅🏾 🤳🏾 💪🏾 🦵🏾 🦶🏾 👂🏾 🦻🏾 👃🏾 👶🏾 👧🏾 🧒🏾 👦🏾 👩🏾 🧑🏾 👨🏾 👩🏾‍🦱 🧑🏾‍🦱 👨🏾‍🦱 👩🏾‍🦰 🧑🏾‍🦰 👨🏾‍🦰 👱🏾‍♀️ 👱🏾 👱🏾‍♂️ 👩🏾‍🦳 🧑🏾‍🦳 👨🏾‍🦳 👩🏾‍🦲 🧑🏾‍🦲 👨🏾‍🦲 🧔🏾 👵🏾 🧓🏾 👴🏾 👲🏾 👳🏾‍♀️ 👳🏾 👳🏾‍♂️ 🧕🏾 👮🏾‍♀️ 👮🏾 👮🏾‍♂️ 👷🏾‍♀️ 👷🏾 👷🏾‍♂️ 💂🏾‍♀️ 💂🏾 💂🏾‍♂️ 🕵🏾‍♀️ 🕵🏾 🕵🏾‍♂️ 👩🏾‍⚕️ 🧑🏾‍⚕️ 👨🏾‍⚕️ 👩🏾‍🌾 🧑🏾‍🌾 👨🏾‍🌾 👩🏾‍🍳 🧑🏾‍🍳",
        "👩🏾‍🦰 🧑🏾‍🦰 👨🏾‍🦰 👱🏾‍♀️ 👱🏾 👱🏾‍♂️ 👩🏾‍🦳 🧑🏾‍🦳 👨🏾‍🦳 👩🏾‍🦲 🧑🏾‍🦲 👨🏾‍🦲 🧔🏾 👵🏾 🧓🏾 👴🏾 👲🏾 👳🏾‍♀️ 👳🏾 👳🏾‍♂️ 🧕🏾 👮🏾‍♀️ 👮🏾 👮🏾‍♂️ 👷🏾‍♀️ 👷🏾 👷🏾‍♂️ 💂🏾‍♀️ 💂🏾 💂🏾‍♂️ 🕵🏾‍♀️ 🕵🏾 🕵🏾‍♂️ 👩🏾‍⚕️ 🧑🏾‍⚕️ 👨🏾‍⚕️ 👩🏾‍🌾 🧑🏾‍🌾 👨🏾‍🌾 👩🏾‍🍳 🧑🏾‍🍳 👨🏾‍🍳 👩🏾‍🎓 🧑🏾‍🎓 👨🏾‍🎓 👩🏾‍🎤 🧑🏾‍🎤 👨🏾‍🎤 👩🏾‍🏫 🧑🏾‍🏫 👨🏾‍🏫 👩🏾‍🏭 🧑🏾‍🏭 👨🏾‍🏭 👩🏾‍💻 🧑🏾‍💻 👨🏾‍💻 👩🏾‍💼 🧑🏾‍💼 👨🏾‍💼 👩🏾‍🔧 🧑🏾‍🔧 👨🏾‍🔧 👩🏾‍🔬 🧑🏾‍🔬 👨🏾‍🔬 👩🏾‍🎨 ",
        " 👨🏾‍🔧 👩🏾‍🔬 🧑🏾‍🔬 👨🏾‍🔬 👩🏾‍🎨 🧑🏾‍🎨 👨🏾‍🎨 👩🏾‍🚒 🧑🏾‍🚒 👨🏾‍🚒 👩🏾‍✈️ 🧑🏾‍✈️ 👨🏾‍✈️ 👩🏾‍🚀 🧑🏾‍🚀 👨🏾‍🚀 👩🏾‍⚖️ 🧑🏾‍⚖️ 👨🏾‍⚖️ 👰🏾‍♀️ 👰🏾 👰🏾‍♂️ 🤵🏾‍♀️ 🤵🏾 🤵🏾‍♂️ 👸🏾 🤴🏾 🥷🏾 🦸🏾‍♀️ 🦸🏾 🦸🏾‍♂️ 🦹🏾‍♀️ 🦹🏾 🦹🏾‍♂️ 🤶🏾 🧑🏾‍🎄 🎅🏾 🧙🏾‍♀️ 🧙🏾 🧙🏾‍♂️ 🧝🏾‍♀️ 🧝🏾 🧝🏾‍♂️ 🧛🏾‍♀️ 🧛🏾 🧛🏾‍♂️ 🧜🏾‍♀️ 🧜🏾 🧜🏾‍♂️ 🧚🏾‍♀️ 🧚🏾 🧚🏾‍♂️ 👼🏾 🤰🏾 🤱🏾 👩🏾‍🍼 🧑🏾‍🍼 👨🏾‍🍼 🙇🏾‍♀️ 🙇🏾 🙇🏾‍♂️ 💁🏾‍♀️ 💁🏾 💁🏾‍♂️ 🙅🏾‍♀️ 🙅🏾 🙅🏾‍♂️ 🙆🏾‍♀️ 🙆🏾 🙆🏾‍♂️ 🙋🏾‍♀️ 🙋🏾 🙋🏾‍♂️ 🧏🏾‍♀️ 🧏🏾 🧏🏾‍♂️ 🤦🏾‍♀️ 🤦🏾 🤦🏾‍♂️ 🤷🏾‍♀️ 🤷🏾 🤷🏾‍♂️ ",
        "🧏🏾 🧏🏾‍♂️ 🤦🏾‍♀️ 🤦🏾 🤦🏾‍♂️ 🤷🏾‍♀️ 🤷🏾 🤷🏾‍♂️ 🙎🏾‍♀️ 🙎🏾 🙎🏾‍♂️ 🙍🏾‍♀️ 🙍🏾 🙍🏾‍♂️ 💇🏾‍♀️ 💇🏾 💇🏾‍♂️ 💆🏾‍♀️ 💆🏾 💆🏾‍♂️ 🧖🏾‍♀️ 🧖🏾 🧖🏾‍♂️ 💃🏾 🕺🏾 🕴🏿 👩🏾‍🦽 🧑🏾‍🦽 👨🏾‍🦽 👩🏾‍🦼 🧑🏾‍🦼 👨🏾‍🦼 🚶🏾‍♀️ 🚶🏾 🚶🏾‍♂️ 👩🏾‍🦯 🧑🏾‍🦯 👨🏾‍🦯 🧎🏾‍♀️ 🧎🏾 🧎🏾‍♂️ 🏃🏾‍♀️ 🏃🏾 🏃🏾‍♂️ 🧍🏾‍♀️ 🧍🏾 🧍🏾‍♂️ 👭🏾 🧑🏾‍🤝‍🧑🏾 👬🏾 👫🏾 🧗🏾‍♀️ 🧗🏾 🧗🏾‍♂️ 🏇🏾 🏂🏾 🏌🏾‍♀️ 🏌🏾 🏌🏾‍♂️ 🏄🏾‍♀️ 🏄🏾 🏄🏾‍♂️",
        "👨🏾‍🦯 🧎🏾‍♀️ 🧎🏾 🧎🏾‍♂️ 🏃🏾‍♀️ 🏃🏾 🏃🏾‍♂️ 🧍🏾‍♀️ 🧍🏾 🧍🏾‍♂️ 👭🏾 🧑🏾‍🤝‍🧑🏾 👬🏾 👫🏾 🧗🏾‍♀️ 🧗🏾 🧗🏾‍♂️ 🏇🏾 🏂🏾 🏌🏾‍♀️ 🏌🏾 🏌🏾‍♂️ 🏄🏾‍♀️ 🏄🏾 🏄🏾‍♂️ 🚣🏾‍♀️ 🚣🏾 🚣🏾‍♂️ 🏊🏾‍♀️ 🏊🏾 🏊🏾‍♂️ ⛹🏾‍♀️ ⛹🏾 ⛹🏾‍♂️ 🏋🏾‍♀️ 🏋🏾 🏋🏾‍♂️ 🚴🏾‍♀️ 🚴🏾 🚴🏾‍♂️ 🚵🏾‍♀️ 🚵🏾 🚵🏾‍♂️ 🤸🏾‍♀️ 🤸🏾 🤸🏾‍♂️ 🤽🏾‍♀️ 🤽🏾 🤽🏾‍♂️ 🤾🏾‍♀️ 🤾🏾 🤾🏾‍♂️ 🤹🏾‍♀️ 🤹🏾 🤹🏾‍♂️ 🧘🏾‍♀️ 🧘🏾 🧘🏾‍♂️ 🛀🏾 🛌🏾",
        "👋🏿 🤚🏿 🖐🏿 ✋🏿 🖖🏿 👌🏿 🤌🏿 🤏🏿 ✌🏿 🤞🏿 🤟🏿 🤘🏿 🤙🏿 👈🏿 👉🏿 👆🏿 🖕🏿 👇🏿 ☝🏿 👍🏿 👎🏿 ✊🏿 👊🏿 🤛🏿 🤜🏿 👏🏿 🙌🏿 👐🏿 🤲🏿 🙏🏿 ✍🏿 💅🏿 🤳🏿 💪🏿 🦵🏿 🦶🏿 👂🏿 🦻🏿 👃🏿 👶🏿 👧🏿 🧒🏿 👦🏿 👩🏿 🧑🏿 👨🏿 👩🏿‍🦱 🧑🏿‍🦱 👨🏿‍🦱 👩🏿‍🦰 🧑🏿‍🦰 👨🏿‍🦰 👱🏿‍♀️ 👱🏿 👱🏿‍♂️ 👩🏿‍🦳 🧑🏿‍🦳 👨🏿‍🦳 👩🏿‍🦲 🧑🏿‍🦲 👨🏿‍🦲 🧔🏿 👵🏿 🧓🏿 👴🏿 👲🏿 👳🏿‍♀️ 👳🏿 👳🏿‍♂️ 🧕🏿 👮🏿‍♀️ 👮🏿 👮🏿‍♂️ 👷🏿‍♀️ ",
        "👷🏿‍♀️ 👷🏿 👷🏿‍♂️ 💂🏿‍♀️ 💂🏿 💂🏿‍♂️ 🕵🏿‍♀️ 🕵🏿 🕵🏿‍♂️ 👩🏿‍⚕️ 🧑🏿‍⚕️ 👨🏿‍⚕️ 👩🏿‍🌾 🧑🏿‍🌾 👨🏿‍🌾 👩🏿‍🍳 🧑🏿‍🍳 👨🏿‍🍳 👩🏿‍🎓 🧑🏿‍🎓 👨🏿‍🎓 👩🏿‍🎤 🧑🏿‍🎤 👨🏿‍🎤 👩🏿‍🏫 🧑🏿‍🏫 👨🏿‍🏫 👩🏿‍🏭 🧑🏿‍🏭 👨🏿‍🏭 👩🏿‍💻 🧑🏿‍💻 👨🏿‍💻 👩🏿‍💼 🧑🏿‍💼 👨🏿‍💼 👩🏿‍🔧 🧑🏿‍🔧 👨🏿‍🔧 👩🏿‍🔬 🧑🏿‍🔬 👨🏿‍🔬 👩🏿‍🎨 🧑🏿‍🎨 👨🏿‍🎨 👩🏿‍🚒 🧑🏿‍🚒 👨🏿‍🚒 👩🏿‍✈️ 🧑🏿‍✈️ 👨🏿‍✈️ 👩🏿‍🚀 🧑🏿‍🚀 👨🏿‍🚀 👩🏿‍⚖️ 🧑🏿‍⚖️ 👨🏿‍⚖️ 👰🏿‍♀️ 👰🏿 ",
        "👰🏿 👰🏿‍♂️ 🤵🏿‍♀️ 🤵🏿 🤵🏿‍♂️ 👸🏿 🤴🏿 🥷🏿 🦸🏿‍♀️ 🦸🏿 🦸🏿‍♂️ 🦹🏿‍♀️ 🦹🏿 🦹🏿‍♂️ 🤶🏿 🧑🏿‍🎄 🎅🏿 🧙🏿‍♀️ 🧙🏿 🧙🏿‍♂️ 🧝🏿‍♀️ 🧝🏿 🧝🏿‍♂️ 🧛🏿‍♀️ 🧛🏿 🧛🏿‍♂️ 🧜🏿‍♀️ 🧜🏿 🧜🏿‍♂️ 🧚🏿‍♀️ 🧚🏿 🧚🏿‍♂️ 👼🏿 🤰🏿 🤱🏿 👩🏿‍🍼 🧑🏿‍🍼 👨🏿‍🍼 🙇🏿‍♀️ 🙇🏿 🙇🏿‍♂️ 💁🏿‍♀️ 💁🏿 💁🏿‍♂️ 🙅🏿‍♀️ 🙅🏿 🙅🏿‍♂️ 🙆🏿‍♀️ 🙆🏿 🙆🏿‍♂️ 🙋🏿‍♀️ 🙋🏿 🙋🏿‍♂️ 🧏🏿‍♀️ 🧏🏿 🧏🏿‍♂️ 🤦🏿‍♀️ 🤦🏿 🤦🏿‍♂️ 🤷🏿‍♀️ 🤷🏿 🤷🏿‍♂️ 🙎🏿‍♀️ 🙎🏿 🙎🏿‍♂️ 🙍🏿‍♀️ 🙍🏿 🙍🏿‍♂️ 💇🏿‍♀️ 💇🏿",
        "💇🏿 💇🏿‍♂️ 💆🏿‍♀️ 💆🏿 💆🏿‍♂️ 🧖🏿‍♀️ 🧖🏿 🧖🏿‍♂️ 💃🏿 🕺🏿 🕴🏿 👩🏿‍🦽 🧑🏿‍🦽 👨🏿‍🦽 👩🏿‍🦼 🧑🏿‍🦼 👨🏿‍🦼 🚶🏿‍♀️ 🚶🏿 🚶🏿‍♂️ 👩🏿‍🦯 🧑🏿‍🦯 👨🏿‍🦯 🧎🏿‍♀️ 🧎🏿 🧎🏿‍♂️ 🏃🏿‍♀️ 🏃🏿 🏃🏿‍♂️ 🧍🏿‍♀️ 🧍🏿 🧍🏿‍♂️ 👭🏿 🧑🏿‍🤝‍🧑🏿 👬🏿 👫🏿 🧗🏿‍♀️ 🧗🏿 🧗🏿‍♂️ 🏇🏿 🏂🏿 🏌🏿‍♀️ 🏌🏿 🏌🏿‍♂️ 🏄🏿‍♀️ 🏄🏿 🏄🏿‍♂️ 🚣🏿‍♀️ 🚣🏿 🚣🏿‍♂️ 🏊🏿‍♀️ 🏊🏿 🏊🏿‍♂️ ⛹🏿‍♀️ ⛹🏿 ⛹🏿‍♂️ 🏋🏿‍♀️ 🏋🏿 🏋🏿‍♂️ 🚴🏿‍♀️",
        "🏋🏿‍♂️ 🚴🏿‍♀️ 🚴🏿 🚴🏿‍♂️ 🚵🏿‍♀️ ⚫️ ⚪️ 🟤 🔺 🔻 🔸 🔹 🔶 🔷 🔳 🔲 ▪️ ▫️ ◾️ ◽️ ◼️ ◻️ 🟥 🟧 🟨 🟩 🟦 🟪 ⬛️ ⬜️ 🟫 🔈 🔇 🔉 🔊 🔔 🔕 📣 📢 👁‍🗨 💬 💭 🗯 ♠️ ♣️ ♥️  🚵🏿 🚵🏿‍♂️ 🤸🏿‍♀️ 🤸🏿 🤸🏿‍♂️ 🤽🏿‍♀️ 🤽🏿 🤽🏿‍♂️ 🤾🏿‍♀️ 🤾🏿 🤾🏿‍♂️ 🤹🏿‍♀️ 🤹🏿 🤹🏿‍♂️ 🧘🏿‍♀️ 🧘🏿 🧘🏿‍♂️ 🛀🏿 🛌🏿",
        "🐶 🐱 🐭 🐹 🐰 🦊 🐻 🐼 🐻‍❄️ 🐨 🐯 🦁 🐮 🐷 🐽 🐸 🐵 🙈 🙉 🙊 🐒 🐔 🐧 🐦 🐤 🐣 🐥 🦆 🦅 🦉 🦇 🐺 🐗 🐴 🦄 🐝 🪱 🐛 🦋 🐌 🐞 🐜 🪰 🪲 🪳 🦟 🦗 🕷 🕸 🦂 🐢 🐍 🦎 🦖 🦕 🐙 🦑 🦐 🦞 🦀 🐡 🐠 🐟 🐬 🐳 🐋 🦈 🐊 🐅 🐆 🦓 🦍 🦧 🦣 🐘 🦛 🦏 🐪 🐫 🦒 🦘 🦬 🐃 🐂 🐄 🐎 🐖 🐏 🐑 🦙 🐐 🦌",
        "🦞 🦀 🐡 🐠 🐟 🐬 🐳 🐋 🦈 🐊 🐅 🐆 🦓 🦍 🦧 🦣 🐘 🦛 🦏 🐪 🐫 🦒 🦘 🦬 🐃 🐂 🐄 🐎 🐖 🐏 🐑 🦙 🐐 🦌 🐕 🐩 🦮 🐕‍🦺 🐈 🐈‍⬛ 🪶 🐓 🦃 🦤 🦚 🦜 🦢 🦩 🕊 🐇 🦝 🦨 🦡 🦫 🦦 🦥 🐁 🐀 🐿 🦔 🐾 🐉 🐲 🌵 🎄 🌲 🌳 🌴 🪵 🌱 🌿 ☘️ 🍀 🎍 🪴 🎋 🍃 🍂",
        "🎍 🪴 🎋 🍃 🍂 🍁 🍄 🐚 🪨 🌾 💐 🌷 🌹 🥀 🌺 🌸 🌼 🌻 🌞 🌝 🌛 🌜 🌚 🌕 🌖 🌗 🌘 🌑 🌒 🌓 🌔 🌙 🌎 🌍 🌏 🪐 💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥 🌪 🌈 ☀️ 🌤 ⛅️ 🌥 ☁️ 🌦 🌧 ⛈ 🌩 🌨 ❄️ ☃️ ⛄️ 🌬 💨 💧 💦",
        "🐿 🦔 🐾 🐉 🐲 🌵 🎄 🌲 🌳 🌴 🪵 🌱 🌿 ☘️ 🍀 🎍 🪴 🎋 🍃 🍂 🍁 🍄 🐚 🪨 🌾 💐 🌷 🌹 🥀 🌺 🌸 🌼 🌻 🌞 🌝 🌛 🌜 🌚 🌕 🌖 🌗 🌘 🌑 🌒 🌓 🌔 🌙 🌎 🌍 🌏 🪐 💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥 🌪 🌈 ☀️ 🌤 ⛅️ 🌥 ☁️ 🌦 🌧 ⛈ 🌩 🌨 ❄️ ☃️ ⛄️ 🌬 💨 💧 💦 ☔️ ☂️ 🌊 🌫",
        "🍏 🍎 🍐 🍊 🍋 🍌 🍉 🍇 🍓 🫐 🍈 🍒 🍑 🥭 🍍 🥥 🥝 🍅 🍆 🥑 🥦 🥬 🥒 🌶 🫑 🌽 🥕 🫒 🧄 🧅 🥔 🍠 🥐 🥯 🍞 🥖 🥨 🧀 🥚 🍳 🧈 🥞 🧇 🥓 🥩 🍗 🍖 🦴 🌭 🍔 🍟 🍕 🫓 🥪 🥙 🧆 🌮 🌯 🫔 🥗 🥘 🫕 🥫 🍝",
        "🥘 🫕 🥫 🍝 🍜 🍲 🍛 🍣 🍱 🥟 🦪 🍤 🍙 🍚 🍘 🍥 🥠 🥮 🍢 🍡 🍧 🍨 🍦 🥧 🧁 🍰 🎂 🍮 🍭 🍬 🍫 🍿 🍩 🍪 🌰 🥜 🍯 🥛 🍼 🫖 ☕️ 🍵 🧃 🥤 🧋 🍶 🍺 🍻 🥂 🍷 🥃 🍸 🍹 🧉 🍾 🧊 🥄 🍴 🍽 🥣 🥡 🥢 🧂",
        "⚽️ 🏀 🏈 ⚾️ 🥎 🎾 🏐 🏉 🥏 🎱 🪀 🏓 🏸 🏒 🏑 🥍 🏏 🪃 🥅 ⛳️ 🪁 🏹 🎣 🤿 🥊 🥋 🎽 🛹 🛼 🛷 ⛸ 🥌 🎿 ⛷ 🏂 🪂 🏋️‍♀️ 🏋️ 🏋️‍♂️ 🤼‍♀️ 🤼 🤼‍♂️ 🤸‍♀️ 🤸 🤸‍♂️ ⛹️‍♀️ ⛹️ ⛹️‍♂️ 🤺 🤾‍♀️ 🤾 🤾‍♂️ 🏌️‍♀️ 🏌️ 🏌️‍♂️ 🏇 🧘‍♀️ 🧘 🧘‍♂️ 🏄‍♀️ 🏄 🏄‍♂️ 🏊‍♀️ 🏊 🏊‍♂️",
        "🏊‍♀️ 🏊 🏊‍♂️ 🤽‍♀️ 🤽 🤽‍♂️ 🚣‍♀️ 🚣 🚣‍♂️ 🧗‍♀️ 🧗 🧗‍♂️ 🚵‍♀️ 🚵 🚵‍♂️ 🚴‍♀️ 🚴 🚴‍♂️ 🏆 🥇 🥈 🥉 🏅 🎖 🏵 🎗 🎫 🎟 🎪 🤹 🤹‍♂️ 🤹‍♀️ 🎭 🩰 🎨 🎬 🎤 🎧 🎼 🎹 🥁 🪘 🎷 🎺 🪗 🎸 🪕 🎻 🎲 ♟ 🎯 🎳 🎮 🎰 🧩",
        "🚗 🚕 🚙 🚌 🚎 🏎 🚓 🚑 🚒 🚐 🛻 🚚 🚛 🚜 🦯 🦽 🦼 🛴 🚲 🛵 🏍 🛺 🚨 🚔 🚍 🚘 🚖 🚡 🚠 🚟 🚃 🚋 🚞 🚝 🚄 🚅 🚈 🚂 🚆 🚇 🚊 🚉 ✈️ 🛫 🛬 🛩 💺 🛰 🚀 🛸 🚁 🛶 ⛵️ 🚤 🛥 🛳 ⛴ 🚢 ⚓️ 🪝 ⛽️ 🚧 🚦 🚥 🚏 🗺 🗿 🗽 🗼 🏰 🏯 🏟 🎡 🎢 🎠 ⛲️ ⛱ 🏖",
        " ⛲️ ⛱ 🏖 🏝 🏜 🌋 ⛰ 🏔 🗻 🏕 ⛺️ 🛖 🏠 🏡 🏘 🏚 🏗 🏭 🏢 🏬 🏣 🏤 🏥 🏦 🏨 🏪 🏫 🏩 💒 🏛 ⛪️ 🕌 🕍 🛕 🕋 ⛩ 🛤 🛣 🗾 🎑 🏞 🌅 🌄 🌠 🎇 🎆 🌇 🌆 🏙 🌃 🌌 🌉 🌁",
        "⌚️ 📱 📲 💻 ⌨️ 🖥 🖨 🖱 🖲 🕹 🗜 💽 💾 💿 📀 📼 📷 📸 📹 🎥 📽 🎞 📞 ☎️ 📟 📠 📺 📻 🎙 🎚 🎛 🧭 ⏱ ⏲ ⏰ 🕰 ⌛️ ⏳ 📡 🔋 🔌 💡 🔦 🕯 🪔 🧯 🛢 💸 💵 💴 💶 💷 🪙 💰 💳 💎 ⚖️ 🪜 🧰 🪛 🔧 🔨 ⚒ 🛠 ⛏ 🪚 🔩 ⚙️ 🪤 🧱 ⛓ 🧲 🔫 💣 🧨 🪓 🔪 🗡 ⚔️ 🛡 🚬 ⚰️ ",
        "🚬 ⚰️ 🪦 ⚱️ 🏺 🔮 📿 🧿 💈 ⚗️ 🔭 🔬 🕳 🩹 🩺 💊 💉 🩸 🧬 🦠 🧫 🧪 🌡 🧹 🪠 🧺 🧻 🚽 🚰 🚿 🛁 🛀 🧼 🪥 🪒 🧽 🪣 🧴 🛎 🔑 🗝 🚪 🪑 🛋 🛏 🛌 🧸 🪆 🖼 🪞 🪟 🛍 🛒 🎁 🎈 🎏 🎀 🪄 🪅 🎊 🎉 🎎 🏮 🎐 🧧  📅 🗑 📇 🗃 🗳 🗄 📋 📁 📂 🗂 🗞 📰 📓 📔 📒 📕 📗",
        "✉️ 📩 📨 📧 💌 📥 📤 📦 🏷 🪧 📪 📫 📬 📭 📮 📯 📜 📃 📄 📑 🧾 📊 📈 📉 🗒 🗓 📆✉️ 📩 📨 📧 💌 📥 📤 📦 🏷 🪧 📪 📫 📬 📭 📮 📯 📜 📃 📄 📑 🧾 📊 📈 📉 🗒 🗓 📆",
        "🎎 🏮 🎐 🧧 ✉️ 📩 📨 📧 💌 📥 📤 📦 🏷 🪧 📪 📫 📬 📭 📮 📯 📜 📃 📄 📑 🧾 📊 📈 📉 🗒 🗓 📆 📅 🗑 📇 🗃 🗳 🗄 📋 📁 📂 🗂 🗞 📰 📓 📔 📒 📕 📗 📘 📙 📚 📖 🔖 🧷 🔗 📎 🖇 📐 📏 🧮 📌 📍 ✂️ 🖊 🖋 ✒️ 🖌 🖍 📝 ✏️ 🔍 🔎 🔏 🔐 🔒 🔓",
        "❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 💔 ❣️ 💕 💞 💓 💗 💖 💘 💝 💟 ☮️ ✝️ ☪️ 🕉 ☸️ ✡️ 🔯 🕎 ☯️ ☦️ 🛐 ⛎ ♈️ ♉️ ♊️ ♋️ ♌️ ♍️ ♎️ ♏️ ♐️ ♑️ ♒️ ♓️ 🆔 ⚛️ 🉑 ☢️ ☣️ 📴 📳 🈶 🈚️ 🈸 🈺 🈷️ ✴️ 🆚 💮 🉐 ㊙️ ㊗️ 🈴 🈵 🈹 🈲 🅰️ 🅱️ 🆎 🆑 🅾️ 🆘 ❌ ⭕️ 🛑 ⛔️ 📛 🚫",
        "⭕️ 🛑 ⛔️ 📛 🚫 💯 💢 ♨️ 🚷 🚯 🚳 🚱 🔞 📵 🚭 ❗️ ❕ ❓ ❔ ‼️ ⁉️ 🔅 🔆 〽️ ⚠️ 🚸 🔱 ⚜️ 🔰 ♻️ ✅ 🈯️ 💹 ❇️ ✳️ ❎ 🌐 💠 Ⓜ️ 🌀 💤 🏧 🚾 ♿️ 🅿️ 🛗 🈳 🈂️ 🛂 🛃 🛄 🛅 🚹 🚺 🚼 ⚧ 🚻 🚮 🎦 📶 🈁 🔣 ℹ️ 🔤 🔡 🔠 🆖 🆗 🆙 🆒 🆕 🆓 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟 🔢 #️⃣ *️⃣ ⏏️ ▶️ ⏸ ⏯ ⏹ ⏺",
        "2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟 🔢 #️⃣ *️⃣ ⏏️ ▶️ ⏸ ⏯ ⏹ ⏺ ⏭ ⏮ ⏩ ⏪ ⏫ ⏬ ◀️ 🔼 🔽 ➡️ ⬅️ ⬆️ ⬇️ ↗️ ↘️ ↙️ ↖️ ↕️ ↔️ ↪️ ↩️ ⤴️ ⤵️ 🔀 🔁 🔂 🔄 🔃 🎵 🎶 ➕ ➖ ➗ ✖️ ♾ 💲 💱 ™️ ©️ ®️ 〰️ ➰ ➿ 🔚 🔙 🔛 🔝 🔜 ✔️ ☑️ 🔘 🔴 🟠 🟡 🟢 🔵 🟣 ⚫️ ⚪️ 🟤 🔺 🔻 🔸 🔹 🔶 🔷 🔳 🔲 ▪️ ▫️ ◾️ ◽️",
        "🟠 🟡 🟢 🔵 🟣 ⚫️ ⚪️ 🟤 🔺 🔻 🔸 🔹 🔶 🔷 🔳 🔲 ▪️ ▫️ ◾️ ◽️ ◼️ ◻️ 🟥 🟧 🟨 🟩 🟦 🟪 ⬛️ ⬜️ 🟫 🔈 🔇 🔉 🔊 🔔 🔕 📣 📢 👁‍🗨 💬 💭 🗯 ♠️ ♣️ ♥️ ♦️ 🃏 🎴 🀄️ 🕐 🕑 🕒 🕓 🕔 🕕 🕖 🕗 🕘 🕙 🕚 🕛 🕜 🕝 🕞 🕟 🕠 🕡 🕢 🕣 🕤 🕥 🕦 🕧",
        "✢ ✣ ✤ ✥ ✦ ✧ ★ ☆ ✯ ✡︎ ✩ ✪ ✫ ✬ ✭ ✮ ✶ ✷ ✵ ✸ ✹ → ⇒ ⟹ ⇨ ⇾ ➾ ⇢ ☛ ☞ ➔ ➜ ➙ ➛ ➝ ➞ ♠︎ ♣︎ ♥︎ ♦︎ ♤ ♧ ♡ ♢ ♚ ♛ ♜ ♝ ♞ ♟ ♔ ♕ ♖ ♗ ♘ ♙ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ 🂠 ⚈ ⚉ ⚆ ⚇ 𓀀 𓀁 𓀂 𓀃 𓀄 𓀅 𓀆 𓀇 𓀈 𓀉 𓀊 𓀋 𓀌 𓀍 𓀎 𓀏 𓀐 𓀑 𓀒 𓀓 𓀔 𓀕 𓀖 𓀗 𓀘 𓀙 𓀚 𓀛 𓀜 𓀝",
        "🥲 🥸 🤌 🤌🏻 🤌🏼 🤌🏽 🤌🏾 🤌🏿 🫀 🫁 🥷 🤵‍♀️ 🤵🏻‍♀️ 🤵🏼‍♀️ 🤵🏽‍♀️ 🤵🏾‍♀️ 🤵🏿‍♀️ 🤵‍♂️ 🤵🏻‍♂️ 🤵🏼‍♂️ 🤵🏽‍♂️ 🤵🏾‍♂️ 🤵🏿‍♂️ 👰‍♀️ 👰🏻‍♀️ 👰🏼‍♀️ 👰🏽‍♀️ 👰🏾‍♀️ 👰🏿‍♀️ 👰‍♂️ 👰🏻‍♂️ 👰🏼‍♂️ ⚫️ ⚪️ 🟤 🔺 🔻 🔸 🔹 🔶 🔷 🔳 🔲 ▪️ ▫️ ◾️ ◽️ ◼️ ◻️ 🟥 🟧 🟨 🟩 🟦 🟪 ⬛️ ⬜️ 🟫 🔈 🔇 🔉 🔊 🔔 🔕 📣 📢 👁‍🗨 💬 💭 🗯 ♠️ ♣️ ♥️  👰🏽‍♂️ 👰🏾‍♂️ 👰🏿‍♂️",
        "👰🏾‍♂️ 👰🏿‍♂️ 👩‍🍼 👩🏻‍🍼 👩🏼‍🍼 👩🏽‍🍼 👩🏾‍🍼 👩🏿‍🍼 🧑‍🍼 🧑🏻‍🍼 🧑🏼‍🍼 🧑🏽‍🍼 🧑🏾‍🍼 🧑🏿‍🍼 👨‍🍼 👨🏻‍🍼 👨🏼‍🍼 👨🏽‍🍼 👨🏾‍🍼 👨🏿‍🍼 🧑‍🎄 🧑🏻‍🎄 🧑🏼‍🎄 🧑🏽‍🎄 🧑🏾‍🎄 🧑🏿‍🎄 🫂 🐈‍⬛ 🦬 🦣 🦫 🐻‍❄️ 🦤 🪶 🦭 🪲 🪳 🪰 🪱 🪴 🫐 🫒 🫑 🫓 🫔 🫕 🫖 🧋 🪨 🪵 🛖 🛻 🛼 🪄 🪅 🪆 🪡 🪢 🩴 🪖 🪗 🪘 🪙 🪃 🪚 🪛 🪝 🪜 🛗 🪞 🪟 🪠 🪤 🪣 🪥 🪦 🪧 🏳️‍⚧️",
        "😮‍💨 😵‍💫 😶‍🌫️ ❤️‍🔥 ❤️‍🩹 🧔‍♀️ 🧔🏻‍♀️ 🧔🏼‍♀️ 🧔🏽‍♀️ 🧔🏾‍♀️ 🧔🏿‍♀️ 🧔‍♂️ 🧔🏻‍♂️ 🧔🏼‍♂️ 🧔🏽‍♂️ 🧔🏾‍♂️ 🧔🏿‍♂️ 💑🏻 💑🏼 💑🏽 💑🏾 💑🏿 💏🏻 💏🏼 💏🏽 💏🏾 💏🏿 👨🏻‍❤️‍👨🏻 👨🏻‍❤️‍👨🏼 👨🏻‍❤️‍👨🏽 👨🏻‍❤️‍👨🏾 👨🏻‍❤️‍👨🏿 👨🏼‍❤️‍👨🏻 👨🏼‍❤️‍👨🏼 👨🏼‍❤️‍👨🏽 👨🏼‍❤️‍👨🏾 👨🏼‍❤️‍👨🏿 👨🏽‍❤️‍👨🏻 👨🏽‍❤️‍👨🏼 👨🏽‍❤️‍👨🏽 👨🏽‍❤️‍👨🏾 👨🏽‍❤️‍👨🏿 👨🏾‍❤️‍👨🏻 👨🏾‍❤️‍👨🏼 👨🏾‍❤️‍👨🏽 👨🏾‍❤️‍👨🏾 👨🏾‍❤️‍👨🏿 👨🏿‍❤️‍👨🏻 👨🏿‍❤️‍👨🏼 👨🏿‍❤️‍👨🏽 👨🏿‍❤️‍👨🏾 👨🏿‍❤️‍👨🏿 👩🏻‍❤️‍👨🏻 👩🏻‍❤️‍👨🏼 👩🏻‍❤️‍👨🏽 👩🏻‍❤️‍👨🏾 👩🏻‍❤️‍👨🏿 👩🏻‍❤️‍👩🏻 👩🏻‍❤️‍👩🏼 👩🏻‍❤️‍👩🏽 👩🏻‍❤️‍👩🏾 👩🏻‍❤️‍👩🏿 👩🏼‍❤️‍👨🏻 👩🏼‍❤️‍👨🏼 👩🏼‍❤️‍👨🏽 👩🏼‍❤️‍👨🏾 👩🏼‍❤️‍👨🏿 👩🏼‍❤️‍👩🏻 👩🏼‍❤️‍👩🏼 👩🏼‍❤️‍👩🏽 👩🏼‍❤️‍👩🏾 👩🏼‍❤️‍👩🏿 👩🏽‍❤️‍👨🏻 👩🏽‍❤️‍👨🏼 👩🏽‍❤️‍👨🏽 👩🏽‍❤️‍👨🏾 👩🏽‍❤️‍👨🏿",
        "👩🏼‍❤️‍👨🏻 👩🏼‍❤️‍👨🏼 👩🏼‍❤️‍👨🏽 👩🏼‍❤️‍👨🏾 👩🏼‍❤️‍👨🏿 👩🏼‍❤️‍👩🏻 👩🏼‍❤️‍👩🏼 👩🏼‍❤️‍👩🏽 👩🏼‍❤️‍👩🏾 👩🏼‍❤️‍👩🏿 👩🏽‍❤️‍👨🏻 👩🏽‍❤️‍👨🏼 👩🏽‍❤️‍👨🏽 👩🏽‍❤️‍👨🏾 👩🏽‍❤️‍👨🏿 👩🏽‍❤️‍👩🏻 👩🏽‍❤️‍👩🏼 👩🏽‍❤️‍👩🏽 👩🏽‍❤️‍👩🏾 👩🏽‍❤️‍👩🏿 👩🏾‍❤️‍👨🏻 👩🏾‍❤️‍👨🏼 👩🏾‍❤️‍👨🏽 👩🏾‍❤️‍👨🏾 👩🏾‍❤️‍👨🏿 👩🏾‍❤️‍👩🏻 👩🏾‍❤️‍👩🏼 👩🏾‍❤️‍👩🏽 👩🏾‍❤️‍👩🏾 👩🏾‍❤️‍👩🏿 👩🏿‍❤️‍👨🏻 👩🏿‍❤️‍👨🏼 👩🏿‍❤️‍👨🏽 👩🏿‍❤️‍👨🏾 👩🏿‍❤️‍👨🏿 👩🏿‍❤️‍👩🏻 👩🏿‍❤️‍👩🏼 👩🏿‍❤️‍👩🏽 👩🏿‍❤️‍👩🏾 👩🏿‍❤️‍👩🏿 🧑🏻‍❤️‍🧑🏼 🧑🏻‍❤️‍🧑🏽 🧑🏻‍❤️‍🧑🏾 🧑🏻‍❤️‍🧑🏿 🧑🏼‍❤️‍🧑🏻 🧑🏼‍❤️‍🧑🏽 🧑🏼‍❤️‍🧑🏾 🧑🏼‍❤️‍🧑🏿 🧑🏽‍❤️‍🧑🏻 🧑🏽‍❤️‍🧑🏼 🧑🏽‍❤️‍🧑🏾",
        "🧑🏽‍❤️‍🧑🏾 🧑🏽‍❤️‍🧑🏿 🧑🏾‍❤️‍🧑🏻 🧑🏾‍❤️‍🧑🏼 🧑🏾‍❤️‍🧑🏽 🧑🏾‍❤️‍🧑🏿 🧑🏿‍❤️‍🧑🏻 🧑🏿‍❤️‍🧑🏼 🧑🏿‍❤️‍🧑🏽 🧑🏿‍❤️‍🧑🏾 👨🏻‍❤️‍💋‍👨🏻 👨🏻‍❤️‍💋‍👨🏼 👨🏻‍❤️‍💋‍👨🏽 👨🏻‍❤️‍💋‍👨🏾 👨🏻‍❤️‍💋‍👨🏿 👨🏼‍❤️‍💋‍👨🏻 👨🏼‍❤️‍💋‍👨🏼 👨🏼‍❤️‍💋‍👨🏽 👨🏼‍❤️‍💋‍👨🏾 👨🏼‍❤️‍💋‍👨🏿 👨🏽‍❤️‍💋‍👨🏻 👨🏽‍❤️‍💋‍👨🏼 👨🏽‍❤️‍💋‍👨🏽 👨🏽‍❤️‍💋‍👨🏾 👨🏽‍❤️‍💋‍👨🏿 👨🏾‍❤️‍💋‍👨🏻 👨🏾‍❤️‍💋‍👨🏼 👨🏾‍❤️‍💋‍👨🏽 👨🏾‍❤️‍💋‍👨🏾 👨🏾‍❤️‍💋‍👨🏿 👨🏿‍❤️‍💋‍👨🏻 👨🏿‍❤️‍💋‍👨🏼 👨🏿‍❤️‍💋‍👨🏽 👨🏿‍❤️‍💋‍👨🏾 👨🏿‍❤️‍💋‍👨🏿 👩🏻‍❤️‍💋‍👨🏻 👩🏻‍❤️‍💋‍👨🏼 👩🏻‍❤️‍💋‍👨🏽 👩🏻‍❤️‍💋‍👨🏾 👩🏻‍❤️‍💋‍👨🏿",
        "👩🏻‍❤️‍💋‍👨🏿 👩🏻‍❤️‍💋‍👩🏻 👩🏻‍❤️‍💋‍👩🏼 👩🏻‍❤️‍💋‍👩🏽 👩🏻‍❤️‍💋‍👩🏾 👩🏻‍❤️‍💋‍👩🏿 👩🏼‍❤️‍💋‍👨🏻 👩🏼‍❤️‍💋‍👨🏼 👩🏼‍❤️‍💋‍👨🏽 👩🏼‍❤️‍💋‍👨🏾 👩🏼‍❤️‍💋‍👨🏿 👩🏼‍❤️‍💋‍👩🏻 👩🏼‍❤️‍💋‍👩🏼 👩🏼‍❤️‍💋‍👩🏽 👩🏼‍❤️‍💋‍👩🏾 👩🏼‍❤️‍💋‍👩🏿 👩🏽‍❤️‍💋‍👨🏻 👩🏽‍❤️‍💋‍👨🏼 👩🏽‍❤️‍💋‍👨🏽 👩🏽‍❤️‍💋‍👨🏾 👩🏽‍❤️‍💋‍👨🏿 👩🏽‍❤️‍💋‍👩🏻 👩🏽‍❤️‍💋‍👩🏼 👩🏽‍❤️‍💋‍👩🏽 👩🏽‍❤️‍💋‍👩🏾 👩🏽‍❤️‍💋‍👩🏿 👩🏾‍❤️‍💋‍👨🏻 👩🏾‍❤️‍💋‍👨🏼 👩🏾‍❤️‍💋‍👨🏽 👩🏾‍❤️‍💋‍👨🏾 👩🏾‍❤️‍💋‍👨🏿 👩🏾‍❤️‍💋‍👩🏻 👩🏾‍❤️‍💋‍👩🏼 👩🏾‍❤️‍💋‍👩🏽 👩🏾‍❤️‍💋‍👩🏾 👩🏾‍❤️‍💋‍👩🏿 👩🏿‍❤️‍💋‍👨🏻 👩🏿‍❤️‍💋‍👨🏼 👩🏿‍❤️‍💋‍👨🏽 👩🏿‍❤️‍💋‍👨🏾 👩🏿‍❤️‍💋‍👨🏿 👩🏿‍❤️‍💋‍👩🏻 👩🏿‍❤️‍💋‍👩🏼 👩🏿‍❤️‍💋‍👩🏽 👩🏿‍❤️‍💋‍👩🏾 👩🏿‍❤️‍💋‍👩🏿",
        "🧑🏻‍❤️‍💋‍🧑🏼 🧑🏻‍❤️‍💋‍🧑🏽 🧑🏻‍❤️‍💋‍🧑🏾 🧑🏻‍❤️‍💋‍🧑🏿 🧑🏼‍❤️‍💋‍🧑🏻 🧑🏼‍❤️‍💋‍🧑🏽 🧑🏼‍❤️‍💋‍🧑🏾 🧑🏼‍❤️‍💋‍🧑🏿 🧑🏽‍❤️‍💋‍🧑🏻 🧑🏽‍❤️‍💋‍🧑🏼 🧑🏽‍❤️‍💋‍🧑🏾 🧑🏽‍❤️‍💋‍🧑🏿 🧑🏾‍❤️‍💋‍🧑🏻 🧑🏾‍❤️‍💋‍🧑🏼 🧑🏾‍❤️‍💋‍🧑🏽 🧑🏾‍❤️‍💋‍🧑🏿 🧑🏿‍❤️‍💋‍🧑🏻 🧑🏿‍❤️‍💋‍🧑🏼 🧑🏿‍❤️‍💋‍🧑🏽 🧑🏿‍❤️‍💋‍🧑🏾"
    ]
  
@roover.command(name="Lag", description="Crashes shitty operating systems.")
@commands.cooldown(1, 13)
async def lag(ctx, amount: int=None):
        await ctx.message.delete()
        if amount is None:
            em = discord.Embed(title="Amount cannot be none.")
            em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
            em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
            await ctx.send(embed=em, delete_after=5)
            return
        for i in range(int(amount)):
            await ctx.send(random.choice(lag_chat))

@roover.command(name="Flood", description="Floods the chat.")
@commands.cooldown(1, 120)
async def flood(ctx):
  await ctx.message.delete()
  for i in range(250):
    try:
      await ctx.send("** **\n"*320)
      time.sleep(.1)
    except:
      pass

@roover.command(name="Spam", description="Constantly sends the same message.")
@commands.cooldown(1, 15)
async def spam(ctx, number, *, message):
  await ctx.message.delete()
  for i in range(int(number)):
    try:
      await ctx.send(str(message))
    except:
      pass

@roover.command(name="Massdm", description="Dms all friends a message.")
@commands.cooldown(1, 30)
async def massdm(ctx, *, message):
  await ctx.message.delete()
  for friend in roover.user.friends:
    try:
      await friend.send(message)
    except:
      pass

@roover.command(name="Tping", description="Sends a 'everyone' ping even if permission is disabled.")
async def tping(ctx):
  if len(ctx.guild.members) > 20:
    em = discord.Embed(title=f"An Error Has Occurred:", description=f"Server too big to execute.")
    em.set_footer(text="𝗠𝗮𝗱𝗲 𝗯𝘆 𝗥𝗼𝗼𝘃𝗲𝗿")
    em.set_author(name=f"{roover.user.name}", icon_url=f"{roover.user.avatar_url}")
    await ctx.send(embed=em, delete_after=10)
  else:
    for member in ctx.guild.members:
      pass

@roover.command(name="Rping", description="Tries to ping every server role.")
async def rping(ctx):
  for role in ctx.guild.roles:
    the = "".join(role.id)

@roover.command(name="Sex", description="Fucking stupid shit Shell added.")
async def sex(ctx):
  await ctx.message.delete()
  message = await ctx.send("*Pushes you onto the bed.* 'Sorry baby, but I've been wanting your cock for the past year, I won't miss this chance'")
  await asyncio.sleep(4.5)
  await message.edit(content="'No one will hear you scream, so don't even try to run :smiling_imp:'")
  await asyncio.sleep(3.5)
  await message.edit(content="*I edge closer to you, where both are noses touch together*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I dive into your lips, delivering the feeling of wetness and taste of cherry.*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I begin to devour you, placing my hand behind your neck*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I forcefully gouge my tongue into your mouth, making out with you like no tomorrow*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You reluctantly go along with it, as you have no choice in the matter*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I begin to slowly undress you, pulling off your shirt, revealing your cute pink little nipples*")

  await asyncio.sleep(4.5)
  await message.edit(content="'Aww your so cute :flushed:'")
  await asyncio.sleep(3.5)
  await message.edit(content="*I begin to lick at your nipples, smiling and teasing you*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You begin to feel flustered, as a feeling of warmth pulses through your body*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I suck on your soft, tiny little nipples. You body begins to quiver in pleasure*")
  await asyncio.sleep(3.5)
  await message.edit(content="*After sucking your nipples, I begin to go lower to your stomach*")
  await asyncio.sleep(3.5)

  await message.edit(content="*Our hearts beating faster and faster, I begin to slowly move my hands to your nether regions*")
  
  await asyncio.sleep(3.5)
  await message.edit(content="*I Unzip your pants, releasing your monster thick muscular penis into view, I drool with delight* :drool:")
  await asyncio.sleep(4.5)
  await message.edit(content="*I Slowly and seductively place my hands around the base of your cock, looking deeply into your eyes*")
  await asyncio.sleep(3.5)
  await message.edit(content="'You know you want this right :flushed:. Don't worry, I'll be gentle :smirk:'")
  await asyncio.sleep(3.2)
  
  await message.edit(content="*Begins to slowly stroke cock, mesmerising you and making you feel wanted for once in your deep and sad life*")
  await asyncio.sleep(4.5)
  await message.edit(content="'Damn baby, I didn't know you liked it like that'")
  await asyncio.sleep(3.5)

  await message.edit(content="*Your cock begins to pulsate, you moan in pleasure as my hands slowly stroke up and down your long thick shaft*")
  await asyncio.sleep(4.5)
  await message.edit(content="'UwU I can feel you struggling already :flushed:. Don't worry I'll go slowly'")
  await asyncio.sleep(3.5)
  await message.edit(content="*My soft silky hands begin to gyrate along your thick meaty shaft, as I look deeply into your eyes*")
  await asyncio.sleep(3.5)

  await message.edit(content="*My hands reach the head of your cock, teasing your tip, a small dose of pre-cum escapes*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I seductively head towards the tip of your massive cock, I lick the juicy pre-cum, swirling my tongue around the tip*")
  await asyncio.sleep(4.5)
  await message.edit(content="*You begin to moan in delight,'You like that baby?'*")
  await asyncio.sleep(3.5)

  await message.edit(content="*I begin to speed up slowly, twisting and turning my hands as it passes up and down your cock, you bite your lip in pleasure*")
  await asyncio.sleep(4.5)
  await message.edit(content="*I place my mouth on the head of your cock, my saliva drooling down your hot long shaft, it lubricates your cock*")
  await asyncio.sleep(3.5)
  await message.edit(content="*My mouth begins to lower, gyrating around the tip to the bottom of your cock, I begin to play with your balls*")
  await asyncio.sleep(4.5)
  await message.edit(content="*I pull you deeper inside me, while I stare deeply into your eyes*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You hit against my Uvula and my throat gags over the shaft of your peepee*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I then pulse back, and begin to move up and down your long thick shaft*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You begin to scream, begging me to make you cum*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I say 'no, that's fucking gay bruv, only in my bussy'*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I pull out your penis, and I turn my big booty towards you*")
  await asyncio.sleep(3.5)
  await message.edit(content="*'Your going to cum right here :smirk: No Homo obviously'*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You force your dick into my tight bussy wussy*")
  await asyncio.sleep(3.5)
  await message.edit(content="*I moan in delight at the feeling of your large tool fill my insides OwO*")
  await asyncio.sleep(4.5)
  await message.edit(content="*You begin to thrust hard and fast inside me*")
  await asyncio.sleep(3.5)
  await message.edit(content="*C-Chill daddy, your going to make me cum :flushed: :hot_face:*")
  await asyncio.sleep(4.5)
  await message.edit(content="*You push harder into me, each thrust making my head go crazy*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You begin to scream in an overload of euphoria*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You cum inside me, filling up my bussy in your thick sticky juice*")
  await asyncio.sleep(4.5)
  await message.edit(content="*I cum hard spraying it all over the bed*")
  await asyncio.sleep(3.5)
  await message.edit(content="*You watch me in awe, at the utter beauty you have just seen*")

  await asyncio.sleep(3.5)
  await message.edit(content="*You moan louder, motivating me to go further beyond, I turn into super saiyan 3 goku*")
  await asyncio.sleep(3.5)
  await message.edit(content="https://www.youtube.com/watch?v=kVdlBxdqv8s\n**PS: You are now gay, nothing will save you now**")

@roover.command(name="Cum", description="Just cums.")
async def cum(ctx):
        await ctx.message.delete()
        message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
        await asyncio.sleep(1.2)
        await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
        await asyncio.sleep(1.1)
        await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
        await asyncio.sleep(1.3)
        await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
        await asyncio.sleep(1.2)
        await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
        await asyncio.sleep(1.2)
        await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
        await asyncio.sleep(1.2)
        await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
        await asyncio.sleep(1.3)
        await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
        await asyncio.sleep(1.1)
        await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
