# -*- coding: utf-8 -*- 
###################################################
#__________                                 
#\______   \ ____   _______  __ ___________ 
# |       _//  _ \ /  _ \  \/ // __ \_  __ \
# |    |   (  <_> |  <_> )   /\  ___/|  | \/
# |____|_  /\____/ \____/ \_/  \___  >__|   
# 
# By: Roover & Shell | Message from the Developer:
###################################################
#                  # Warning #                    #
#   Don't edit any of the code below unless you know exactly what you are doing. I am not responsible for any alterations to the script and their affects on it's functions. I will not refund you if you break the bot's code so be mindful. #
###################################################
# Main Imports & Functions #
###################################################
import os 
import json
import sys
###################################################
def warn(*args, **kwargs):
  pass
with open('ODev/dev.json') as devjs:
    devjson = json.load(devjs)
    pycache = devjson.get('caching')
    if str(pycache) == "true":
      pass 
    elif str(pycache) == "false":
      sys.dont_write_bytecode = True
    else:
      os.system("cls" if os.name == "nt" else "clear")
      print(f"\nCritical error encountered. Invalid dev input entered. \nUnless you know exactly what you're doing, don't edit dev.json.\nOtherwise, your input values should be true or false. \nBe sure to also read the manual.txt file for more info.")
      os._exit(4)
###################################################
try:
  from Resources import *
  import warnings
  warnings.warn = warn
  from datetime import datetime
  from colorama import Fore as coloring, init
  init()
  if sys.platform == "win32":
    from dotenv import load_dotenv
    load_dotenv()
  os.system("cls" if os.name == "nt" else "clear")
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  if sys.platform == "win32":
      os.system(f'title RooverCord : {current_time}')
except Exception as e:
  handler(e).efilter()
  os._exit(1)
###################################################
try: 
  import asyncio
  from bot import roover
  import requests
  import httpx
  import getpass
  import time
except Exception as e:
  handler(e).efilter()
  os._exit(1)
###################################################
if os.name == "nt":
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
###################################################
if __name__ == '__main__':
  tried = 0
  tascii1()
  while True:
    verify = getpass.getpass(prompt=f"""\n{coloring.BLUE}┌──{coloring.BLUE}「{coloring.RED}Enter[Ω]Password{coloring.BLUE}」-[{coloring.YELLOW}!{coloring.BLUE}]{coloring.WHITE}:{coloring.BLUE}
└─{coloring.MAGENTA}${coloring.WHITE}: """, stream=None)
    if verify == os.getenv('PASSWORD'):
      print(f"{coloring.BLUE}─────────────────────────────")
      os.system("cls" if os.name == "nt" else "clear")
      break
    elif tried == 2:
      os._exit(8)
    else:
      tried += 1
      pass
  token = os.getenv('TOKEN')
  try:
    roover.run(token, bot=False, reconnect=True)
  except Exception as e:
    tascii1()
    handler(e).efilter()
    # Returns here
###################################################
# Dev Notes #
##################################################
# Use an ExploitDB format to toggle commands.
# Errorcache file: Resources/utils/errorcache.txt
# Basically the efilter function checks if the error is in the error list until it has checked the whole list. The logic behind this is that it wont spam error-cache all the time until the process is done.
# The loop issue is either in bot.run, or the class. The issue was bot.run because I set token as string which fucked it all.
# Shit to add:
# block bypass, follow channel without access.
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) solved weird token error.
# Experiment with threads.
