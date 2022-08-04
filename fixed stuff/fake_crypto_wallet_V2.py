import time, sys, random, os

def clr():
    return os.system("clear")

def print_logo():
    print("""
        ________  __       _____ __             __         
       / ____/ /_/ /_     / ___// /____  ____ _/ /__  _____
      / __/ / __/ __ \    \__ \/ __/ _ \/ __ `/ / _ \/ ___/
     / /___/ /_/ / / /   ___/ / /_/  __/ /_/ / /  __/ /    
    /_____/\__/_/ /_/   /____/\__/\___/\__,_/_/\___/_/     
                                                           
    #FIXED BY SynnK                #MADE BY blob#0005""")

def printf(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.040)
    sys.stdout.write("\n")

def eth():
    printf("Connecting To Api")
    r1 = random.randint(20, 50)
    printf("Starting " + str(r1) + " Server(s)")
    printf("Server(s) Started")
    printf("Sending Crypto Address To Server(s)")
    printf("Started Overclocking On Server(s)")
    printf("Starting In 3 Seconds")
    time.sleep(3)

    # easier way to append upper and lower case instead of adding a list with all the letters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    choice = []
    for i in letters:
        choice.append(i)
        choice.append(i.lower())
    
    for u in range(150):
        clr()
        print_logo()
        rc = random.choices(choice, k=64)
        print("Generated Code - " + "".join(rc) + " - 0.00$")
        time.sleep(0.075)

    clr()
    r1 = random.randint(1644, 9856)
    rc = random.choices(choice, k=64)
    print_logo()
    print("Generated Code - " + "".join(rc) + " - " + str(r1) + "$")
    print("Sending Money To Main Address")
    print("Enough For Today, CYA")
    return

def main():
    print("""
    1. Credits
    2. Change Address
    3. Etherium Stealer""")
    main = input("> ")
    if main == "3":
        eth()
    if main == "1":
        print("Program Was Fully Coded By blob#0005 (shitty code fixed by SynnK)")
        input("Type anything to go back...")
        main()
    if main == "2":
        main = input("Enter Ur Crypto Address: ")
    
main()