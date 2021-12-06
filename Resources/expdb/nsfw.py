import httpx
import json
import os
import time
from colorama import Fore as coloring
token = os.getenv("TOKEN")
###################################################
class bypass:
  def __init__(self, tid):
    self.token = token
    self.tid = tid

  def getting(self):
    try:
      bop = httpx.get(f"https://discord.com/api/v9/channels/{self.tid}/messages?limit=50", headers={'authorization':self.token})
      data_accepted = json.loads(bop.text)
      for z in data_accepted:
        print(f"{z['author']['username']}#{z['author']['discriminator']} : {z['content']}")
      time.sleep(9)
    except:
      print(f"{coloring.RED}「Invalid ID/Token Error」{coloring.RESET}")

  def sending(self, cont):
    try:
      h = httpx.post(f"https://discord.com/api/v9/channels/{self.tid}/messages", headers={'authorization':token}, json={'content': cont, 'tts': False})
      if h.status_code == 200 or 204:
        print(f"{coloring.LIGHTGREEN_EX}「Message Sent Successfully」{coloring.RESET}")
      else:
        print(f"{coloring.RED}「Messasge Failed to Send」{coloring.RESET}")
      time.sleep(3)
    except:
      print(f"{coloring.RED}「Invalid ID Target Inputted」{coloring.RESET}")
