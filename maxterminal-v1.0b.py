commandList = ["help", "text", "reset", "exit", "date", "timeshow", "dateshow", "random"]
timeHour = "12"
timeMin = "00"
from time import gmtime, strftime
import time
import random
print("maxterminal 1.0 Beta")
print("Copyright, maxhatei2 2022 - 2023")
print("Type help for commands. ")
while True:
    UserCommand = input(">>>").lower()
    if UserCommand == "help":
        print("Commands:")
        print("help - Lists all commands available.")
        print("text - The text you will type when the command is running will be repeated.")
        print("exit - Exits maxterminal.")
        print("time - Shows country global time. (GMT)")
        UserCommand = input(">>>").lower()
    elif UserCommand == "text":
        Text = input("Enter text to repeat:").lower()
        print(Text)
        UserCommand = input(">>>").lower()
    elif UserCommand == "exit":
        exit()
    elif UserCommand == "time":
        print("Local clock: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))
        UserCommand = input(">>>").lower()
    elif UserCommand == "Acd4t%^R4567YGFR7y667UHGFR7fr5678uhgr56756YG":
        dateYear = int(input("Enter date year:"))
        if dateYear <= 1970:
            print("Year is too small.")
            UserCommand = input(">>>").lower()
        if dateYear >= 2050:
            print("The year is too big.")
    elif UserCommand == "":
        UserCommand = input(">>>").lower()
    else:
        print("The command", UserCommand, "does not exist.")
        UserCommand = input(">>>").lower()
