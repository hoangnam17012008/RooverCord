###################################################
# .---. .----..----..-..-..---..---. 
# | |-< | || || || | \  / | |- | |-< 
# `-'`-'`----'`----'  `'  `---'`-'`-
###################################################
from Resources.utils.design import coloring, tascii
import os
class handler:
  def __init__(self, e):
    self.error = str(e)
    self.known = ["No module named", "Improper token"]
    # self.known[#]

  def efilter(self):
    maximum = len(self.known)
    count = 0
    for err in self.known:
      if err in self.error:
        if err == "No module named":
          print(f"\n\n{coloring.RED}Failed to import crucial modules. Please PIP install \nthe listed modules and try again. If the imports are \nstill  unssuccessful, contact the developer.\n")
          with open("Resources/utils/data/errorcache.txt", "a+") as failport:
            failport.write(f"{self.error}\n")
          break
          # handler(self.error).unknown()
        elif err == "Improper token":
          print(f"\n\n{coloring.RED}Critical error encountered. Invalid token provided.\nThe account token provided is missing or invalid. See\nREADME.md for more details.\n")
          os._exit(3)
          # os._exit(1)
      elif err not in self.error and count <= maximum:
        count += 1
        continue
    if count == maximum:
      handler(self.error).unknown()
    else:
      return

  def unknown(self):
    with open("Resources/utils/data/errorcache.txt", 'a+', encoding='utf-8')  as hey:
      hey.write(f"{self.error}\n")
      print(f"\n\n{coloring.RED}Critical error encountered. An unknown error has been \nencountered. For more information view the errorcache \nfile, and the FAQ section of the MD file. If issues \npersist or weren't resolved, please contact the \ndeveloper. To use terminal again, press enter.")
###################################################
