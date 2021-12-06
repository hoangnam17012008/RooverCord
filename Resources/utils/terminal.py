try:
    import time
    import os
    import sys
    from Resources.utils.handling import handler
    #from nsfw import test
    from Resources.expdb.tokentools import unverify, tpass, check_one, nitro
    from Resources.expdb.dos import doser 
    from Resources.expdb.vcdos import first
    from Resources.expdb.nsfw import bypass
    from Resources.expdb.webhook import webf
    from Resources.utils.design import *
    from colorama import Fore as coloring
    from geolite2 import geolite2
    import json
    import functools
    import threading
    import socket
    import httpx
    import getpass
except Exception as e:
    handler(e).efilter()
    os._exit(1)
# Add dotenv imports
token = os.getenv("TOKEN")
###################################################
class work:
    def __init__(self, inp):
        self.command = inp  # Gets command name.

    def parse(self):
        if self.command == "clear":
            os.system("cls" if os.name == "nt" else "clear")
        elif self.command == "exit":
            os._exit(6)  # Closes session but also logs out of bot.
        elif self.command == "ascii":
            os.system("cls" if os.name == "nt" else "clear")
            tascii1()
        elif "echo" == self.command[0:4]:
            try:
                to_ech = self.command.split("echo ")[1]
                print("--> " + to_ech)
            except:
                print(
                    f"{coloring.RED}「Command Missing Arguments」{coloring.RESET}"
                )
        elif "help" == self.command[0:4]:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"""
{coloring.BLUE}Omega Terminal Commands & Info
{coloring.WHITE}
-e/-E : To indicate use of exploit.
--------------------------------------------------
Terminal Commands: [command name] [extra args]
Name:    Description:
echo  [text]   Displays message in terminal.
ping [url]     Checks if a site is up and returns it's status code. 
tcheck [token] Check validity of a Discord token.
ipinf [IP] Extracts info of a given IPV4.
help     Displays this help command.
ascii    Displays OmegaSB ascii art in terminal.
yes      Prints yes 30 times because yes.
exit     Terminates script using os.system.
clear    Removes all text printed in terminal.
--------------------------------------------------
Exploit Commands: -e [command name] [extra args]
Name:    Description:
vcdos [dm/gc] [target id] Preforms voice chat denial of service on target.
unverify [token] Unverifies the email of a user token.
dos      Preforms an actual denial of service on a target IP address.
tpass    Gets token from email and password (sometimes).
nsfw [id] Allows you to get and send messages from and to blocked NSFW channels.
webdel [url] Deletes a webhook with it's URL.
          """)
        elif "ping" == self.command[0:4]:
            try:
                targ = self.command.split("ping ")[1]
                if "http://" in targ or "https://" in targ:  # Checks if you're pinging an actual site.
                    if "https://" in targ:
                        tss = targ.split("https://")[1]
                        tss2 = tss.split("/")[0]
                        site_ip = socket.gethostbyname(tss2)
                        print(f"{coloring.BLUE} Pinging: {site_ip}\n")
                    elif "http://" in targ:
                        tss = targ.split("http://")[1]
                        tss2 = tss.split("/")[0]
                        site_ip = socket.gethostbyname(tss2)
                        print(f"{coloring.BLUE} Pinging: {site_ip}\n")
                    for i in range(5):
                        try:
                            respon = httpx.get(
                                targ)  # If request goes through site is up.
                            print(
                                f"{coloring.RED}「{targ} Response: {respon.status_code}」"
                            )
                            time.sleep(.7)  # Sleeps to prevent fuckery.
                        except:  # Otherwise the site do be gone...
                            print(f"{coloring.RED}「Failed To Reach {targ}」")
                else:
                    print(
                        f"{coloring.RED}「Invalid Target Entered」\n"
                    )  # Ignores if https, http, or www website isn't entered.
            except:
                print(
                    f"{coloring.RED}「Invalid Command-line Input」{coloring.RESET}"
                )
        elif "ipinf" == self.command[0:5]:
            try:
                reader = geolite2.reader()
                location = reader.get(self.command.split("ipinf ")[1])
                a = (location['city']['names']['en'])
                b = (location['continent']['names']['en'])
                c = (location['country']['names']['en'])
                f = (location['registered_country']['names']['en'])
                g = (location['subdivisions'][0]['names']['en'])

                print(f"""{coloring.LIGHTGREEN_EX}
  IP Search Results ({self.command.split("ipinf ")[1]}) 
  City/County: {a}
  Continent: {b}
  Country: {c}
  Registered Country: {f}
  State/Province : {g}
                """)
            except:
                print(f"{coloring.RED}「Invalid IP Inputted」{coloring.RESET}")
        elif "tcheck" == self.command[0:6]:
            try:
                ar = self.command.split("tcheck ")[1]
                check_one(ar)
                time.sleep(.4)
            except:
                print(
                    f"{coloring.RED}「Command Missing Arguments」{coloring.RESET}"
                )
        elif self.command == "yes":
            time.sleep(.3)  # For funni effect.
            for i in range(30):  # stupid shit.
                print(f"{coloring.LIGHTGREEN_EX}yes{coloring.RESET}")
                time.sleep(.5)
        elif "-e" in self.command[0:3]:
            os.system("cls" if os.name == "nt" else "clear")
            skull()
            if "-e vcdos" == self.command[0:8]:
                choice = self.command[9:11]
                targer = self.command[11:31]
                first(choice, targer)
            elif "-e unverify" == self.command[0:11]:
                try:
                    ar = self.command.split("unverify ")[1]
                    unverify(ar)
                except:
                    print(
                        f"{coloring.RED}「Command Missing Arguments」{coloring.RESET}"
                    )
            elif "-e dos" == self.command[0:6]:
                port = input(f"{coloring.BLUE}  ┗> Enter Port: ")
                duration = input(f"{coloring.BLUE}  ┗> Enter Duration: ")
                ip = input(f"{coloring.BLUE}  ┗> Enter IP: ")
                if "." in ip:
                    doser(port, duration, ip).denial()
                else:
                    print(
                        f"{coloring.RED}「Invalid IPV4 Inputted」{coloring.RESET}"
                    )
            elif "-e tpass" == self.command[0:8]:
                email = input(f"{coloring.BLUE} ┗> Enter Email: ")
                password = getpass.getpass(
                    prompt=f'{coloring.BLUE} ┗> Enter Password:')
                tpass(email, password)
            elif "-e nbrute" == self.command[0:9]:
                threading.Thread(target=nitro, args=(token, )).start()
            elif "-e nsfw" == self.command[0:7]:
                try:
                    tid = self.command.split("nsfw ")[1]      

                    decis = str(
                        input(
                            f'{coloring.BLUE} ┗> Enter G to get messages or S to send: '
                        ))
                    if decis.lower() == "s":
                        cont = str(
                            input(
                                f'{coloring.BLUE} ┗> Enter message content: '))
                        bypass(tid).sending(cont)
                    elif decis.lower() == "g":
                        bypass(tid).getting()
                    else:
                        print(
                            f"{coloring.RED}「Invalid Command-line Input」{coloring.RESET}")
                except:
                  print(
                        f"{coloring.RED}「Command Missing Arguments」{coloring.RESET}"
                    )                   
            elif "-e webdel" == self.command[0:9]:
              try:
                wurl = self.command.split("webdel ")[1]
                webf(wurl)
              except:
                print(
                        f"{coloring.RED}「Command Missing Arguments」{coloring.RESET}"
                    )
            else:
                print(
                    f"{coloring.RED}「Invalid Command-line Input」{coloring.RESET}"
                )
                time.sleep(.8)
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
            tascii1()
        elif self.command == "":
            pass
        else:
            print(
                f"{coloring.RED}「Invalid Command-line Input」{coloring.RESET}")
            time.sleep(.8)
# Add pc info
