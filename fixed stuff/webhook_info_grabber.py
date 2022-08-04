import requests
from os import system 

system("title Webhook Info Grabber, Fixed by SynnK    Made By blob#0005,   Github: github.com/blob0005")

def webhook_info():

    r = requests.get(webhook)
    r = r.json()

    try:
        webhook = input("Enter Webhook: ")

        r_check = requests.get(webhook).json
        r_check = str(r_check)

        if "200" in r_check:

            name = r["name"]
            avatar = r["avatar"]
            channel_id = r["channel_id"]
            guild_id = r["guild_id"]
            token = r["token"]
            
            print(f'Webhook Name: {name}\nHas Avatar: {avatar}\nChannel ID: {channel_id}\nGuild ID: {guild_id}Webhook Token: {token}')
            
            input("Press Enter To Close The Program")
            exit()

        else:

            print("Webhook Invalid, Please Enter A Valid One")

    except Exception:

        print("Webhook Invalid, Please Enter A Valid One")

webhook_info()