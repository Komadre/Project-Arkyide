import os
import git
import pyfiglet
import random
#Work in progress
# function wmm = welcome message and menu, for later
def wmm():
    wmm = pyfiglet.figlet_format("Arkyide")
    print(wmm)
    print("Select one of the options: \n")
    print('1. Show all tools')
    print("2. To be continued")
    print("3. Exit")
    userinputmenu = int(input("Enter your choice"))
    if userinputmenu == '1':
        toolslistad()
    elif userinputmenu == '2':
        print("to be continuuuueeed")
    elif userinputmenu == '3':
        print('Exiting...')
        os.system('cls')
        
def toolslistad():
    print("")