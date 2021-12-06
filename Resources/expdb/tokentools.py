########################################################
import httpx
import random
import string
from colorama import Fore as coloring
########################################################
def check_one(token):
    tken = httpx.get('https://discordapp.com/api/v9/auth/login', headers={'authorization': token})
    if tken.status_code == 200:
            print(f"{coloring.LIGHTGREEN_EX}「Inputted Token is Valid」{coloring.RESET}")
    else:
            print(f"{coloring.RED}「Inputted Token is Invalid」") 
      
def unverify(token):
    arminius = httpx.get('https://discordapp.com/api/v9/auth/login', headers={'authorization': token})
    if arminius.status_code == 200:
      cucked = httpx.get('https://discord.com/api/v9/guilds/0/members', headers={'authorization': token})
      if cucked.status_code == 400 or 403:
        print(f"{coloring.LIGHTGREEN_EX}「Unverified the Token」{coloring.RESET}")
      else:
        print(f"{coloring.RED}「Unable to Unverify the Token」")  
    else:
      print(f"{coloring.RED}「Inputted Token is Invalid」")

def nitro(token):
    while True:
      code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
      url = httpx.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem", headers={'authorization':token}, timeout=3)
      if url.status_code == 200:
        print(f"{coloring.LIGHTGREEN_EX}「Claimed Nitro to given Token」{coloring.RESET}")
        break
      else:
        print(f"{coloring.RED}「Invalid Nitro Code Generated」{coloring.RESET}")
        pass
  
def tpass(email, password):
  try:
    k = httpx.post("https://discord.com/api/v9/auth/login", headers={'user-agent':f'Mozilla/5.0 (X11; CrOS aarch64 14150.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.124 Safari/537.36', 'content-type':'application/json'}, json={"login":f"{email}","password":f"{password}","undelete":False,"captcha_key":None,"login_source":None,"gift_code_sku_id":None})
    print(f"{coloring.LIGHTGREEN_EX}「Token: {k['token']}」")
  except:
    print(f"{coloring.RED}「Unable to Retrieve Token」")

