import colorama
import os
import time
from colorama import Fore

logo = """
  ___       ____  _                       
 |_ _|_ __ |  _ \(_)_ __   __ _  ___ _ __ 
  | || '_ \| |_) | | '_ \ / _` |/ _ \ '__|
  | || |_) |  __/| | | | | (_| |  __/ |   
 |___| .__/|_|   |_|_| |_|\__, |\___|_|   
     |_|                  |___/         
        []Coded by @_Yyeu[]
"""

def ipping():
    os.system("cls")
    count = 1
    print(Fore.RED + logo)
    e = input("Enter IP Address: ")
    print(f'You are going to ping {e} enable a vpn if you want to keep your ip hidden.')
    r = input("Do you want to continue? (y/n): ")
    if r == 'y':
        time.sleep(1)
    else:
        print("Exiting ... in 3 seconds")
        time.sleep(1)
        print("Exiting ... in 2 seconds")
        time.sleep(1)
        print("Exiting ... in 1 seconds")
        time.sleep(1)
        print("Exiting ... in 0 seconds")
        exit()
    replies = 0
    replies += 1
    hostname = e
    os.system("cls")
    print("-"*100)
    print("="*100)
    print("-"*100)
    while True:
        response = os.system("ping -n 1 " + hostname + " >nul")
        if response == 0:
            print("\033[1;32;40m" + hostname + " is online!" + " [" +  str(count) + "]" +  '\033[0m')
        else:
            print("\033[31m" + hostname + " is offline!" " [" +  str(count) + "]" +  '\033[0m')
        count += 1
        time.sleep(2)


ipping()
