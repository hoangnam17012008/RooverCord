from colorama import Fore as coloring
from datetime import date
import os
###################################################
# Font is big https://www.askapache.com/online-tools/figlet-ascii/
#https://fsymbols.com/
def tascii(omugus):
  print(f"""{coloring.RED}
██████╗░░█████╗░░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔══██╗
██████╔╝██║░░██║██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
  print(f"{date.today()} | {omugus.the_bot} | Version: {omugus.version}")
  print(f"{coloring.BLUE}─"*49)

def tascii1():
  print(f"""{coloring.RED}
██████╗░░█████╗░░█████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔══██╗
██████╔╝██║░░██║██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
██║░░██║╚█████╔╝╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
  print(f"{coloring.BLUE}─"*49)
  print("\n")

def skull():
  try:
    os.system(f'title RooverCord : Expdb')
  except:
    pass # When polishing add linux support here.
  print(f"{coloring.WHITE}─"*85)
  print(f"""{coloring.WHITE}
            .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
  """)
  print(f"{coloring.WHITE}─"*85 + "\n")

class foundation:
  # discord.__version__
  __version__ = "v2.0"
  __devel__ = "Roover & Shell"
###################################################  
