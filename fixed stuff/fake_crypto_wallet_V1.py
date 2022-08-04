import time, sys, random, os
from os import system

system("title " + "Ethereum Wallet Miner,   Made By blob#0005,   Github: github.com/blob0005")

def print00025(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0025)
    sys.stdout.write("\n")

def print0040(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.040)
    sys.stdout.write("\n")

def eth():
    delay2 = 3
    print00025("""
        ________  __       _____ __             __         
       / ____/ /_/ /_     / ___// /____  ____ _/ /__  _____
      / __/ / __/ __ \    \__ \/ __/ _ \/ __ `/ / _ \/ ___/
     / /___/ /_/ / / /   ___/ / /_/  __/ /_/ / /  __/ /    
    /_____/\__/_/ /_/   /____/\__/\___/\__,_/_/\___/_/     
                                                           
                                    #MADE BY blob#0005""")
    print0040("Connecting To Api")
    r1 = random.randint(20, 50)
    print0040("Starting " + str(r1) + " Server(s)")
    print0040("Server(s) Started")
    print0040("Sending Crypto Address To Server(s)")
    print0040("Started Overclocking On Server(s)")
    print0040("Starting In 3 Seconds")
    time.sleep(3)

    choice = []
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in letters:
        choice.append(i)
        choice.append(i.lower())
    
    while True:
        rc = random.choices(choice, k=64)
        rrr = random.randint(1, 100)
        if rrr == 98:
            print(f"Crypto Wallet Generated    |    {''.join(rc)}   |    Code Valid")
            ramount = random.uniform(0.00, 19.00)
            ramount = str(ramount)
            ramount = ramount[:-8]
            print(f"User Had {ramount} Bitcoin(s)")
            time.sleep(delay2)
            print("Sending Bitcoin To Main Address")
            print("Succsesfully Sent")
            print("Enough For Today CYA")
            time.sleep(5)
            exit()
        else:
            print(f"Crypto Wallet Generated    |   {''.join(rc)}   |    Code Invalid")
        time.sleep(0.005)
eth()