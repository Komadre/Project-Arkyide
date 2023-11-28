import os
from os import system
from git import repo
import pyfiglet
from time import sleep
#Work in progress
# function wmm = welcome message and menu, for later
def wmm():
    wmm = pyfiglet.figlet_format("Arkyide")
    print(wmm)
    print("Select one of the options: \n")
    print('1. Show all tools')
    print("2. To be continued")
    print("3. Exit")
    userinputmenu = input("Enter your choice: \n ")
    if userinputmenu == '1':
        os.system('clear')
        toolslistad()
    elif userinputmenu == '2':
        print("to be continuuuueeed")
        sleep(3)
        os.system('clear')
        wmm()
    elif userinputmenu == '3':
        print('Exiting...')
        os.system('clear')
        exit()
    else:
        print("Wrong choice/unknown!")
        sleep(1)
        os.system('clear')
        wmm()
def toolslistad():
    print("")





start = input('Start the script? \n Yes \n No')
if start == 'yes':
    os.system('clear')
    wmmm()


