import requests
from colorama import Fore as coloring
#####################################################
def webf(wurl):
  fucers = str(wurl)
  r = requests.delete(fucers)
  if r.status_code == 204 or 200:
    print(f"{coloring.LIGHTGREEN_EX}「Deletion Successful: {r.status_code}」{coloring.RESET}")
  else:
    print(f"{coloring.RED}「Invalid Webhook Target Inputted」{coloring.RESET}")
