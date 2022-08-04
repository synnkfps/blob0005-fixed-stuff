error = False
from secrets import choice
import sys, time, random, os 
from os import system

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

def print0040f(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.00000005)
    sys.stdout.write("\n")

def print0040e(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.00000005)
    sys.stdout.write("\n")

print00025("""
    _   ___ __                  
   / | / (_) /__________        
  /  |/ / / __/ ___/ __ \       
 / /|  / / /_/ /  / /_/ /       
/_/_|_/_/\__/_/_  \____/        
  / ___/____  (_)___  ___  _____
  \__ \/ __ \/ / __ \/ _ \/ ___/
 ___/ / / / / / /_/ /  __/ /    
/____/_/ /_/_/ .___/\___/_/     
            /_/                 
    MADE  BY  blob#0005
    > FIXED BY SynnK  <""")

print0040("Loading Api...")
print0040("Starting Proxys...")
print0040("Started Api And Proxys")
print0040("Starting Gen In 3 Seconds...")

time.sleep(3)
done = 0
ee = random.randint(15, 20)


choices = []
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in letters:
    choices.append(i)
    choices.append(i.lower())

invalid_code = ""
valid_code = ''.join(random.choice(choices) for i in range(1, 16))

i = 0

for i in range(1, 16):
    invalid_code = ''.join(random.choice(choices) for i in range(1, 16))
    done += 1
    print0040f(f"[{done}] Generated Invalid Code: https://discord.gift/{invalid_code}")
    i += 1

done += 1
print0040e(f"[{done}] Generated Valid Code: https://discord.gift/{valid_code}")
print0040e("Succsesfully Redeemed Nitro To Account")
print0040e("CYA")

time.sleep(5)

exit()