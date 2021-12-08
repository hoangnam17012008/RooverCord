from Resources import *
import httpx
import sys
from colorama import Fore as coloring
import random
import os
import time
import threading
import json
if sys.platform == "win32" or "cygwin":
    from dotenv import load_dotenv
    load_dotenv()
#####################################################
#####################################################
def fluff(furk, conte):
    token = os.getenv("TOKEN")
    strin = httpx.post("https://discord.com/api/v9/users/@me/channels", json={ 'recipients': [furk]}, headers={'authorization': token})
    try:
        ideyee = strin.json()['id']
        ch = httpx.post(f"https://discord.com/api/v9/channels/{ideyee}/messages", headers={'authorization': token}, json={'content': conte})
        if ch.status_code == 200 or 204:
            print(f"{coloring.LIGHTGREEN_EX}「Message Sent Successfully」{coloring.RESET}")
        else:
            print(f"{coloring.RED}「Message Failed to Send」{coloring.RESET}")
    except:
        print(f"{coloring.RED}「Invalid ID Target Inputted」{coloring.RESET}")
