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
    print(strin.status_code)
    try:
        ideyee = strin.json()['id']
        print(ideyee)
        ch = httpx.post(f"https://discord.com/api/v9/channels/{ideyee}/messages", headers={'authorization': token}, json={'content': conte})
        print(ch.status_code)
    except:
        print(f"{coloring.RED}「Invalid ID Target Inputted」{coloring.RESET}")
