import webbrowser
import time
import os
from shutil import copyfile
print("=========== AnyDown Generator 0.95 Beta - WELCOME! ===========")
time.sleep(1)
print("FOLLOW INSTRUCTIONS OR IT WILL NOT WORK")
time.sleep(2)
print("Checking environment...")
if os.path.exists("data\\anydown_packed.exe"):
    print("All set, let's continue!")
else:
    print("anydown_packed.exe main executable does not exists. Aborting...")
    time.sleep(3)
    exit()
time.sleep(3)
print("1. Write a message to the bot, with any text")
print("2. Press enter here. A browser window will open. This is the bot log.")
print("3. Search for the message you wrote (usually is at the end of the page)")
print("4. Copy and paste here the number after 'id:'")
print("Example:")
print("If in the log there is {\"id\":123456 then paste here 123456")
print("Did you understand? Press enter when you are ready.\n")
input()
webbrowser.open("https://api.telegram.org/bot1267083900:AAEddgZ-cH6xl-A2IRZI7bPm2i6lMl6SN5Q/getUpdates")
print("\nPaste the chat id here:")
chatid = input()
try:
    val = int(chatid)
except ValueError:
    print("Nope. The chat id must be an integer. Read the instruction again.")
    print("Aborting...")
    time.sleep(3)
    exit()

if os.path.exists("data\\chatid.dat"):
    os.remove("data\\chatid.dat")
chatidfile = open("data\\chatid.dat", "w+")
chatidfile.write(chatid)
chatidfile.close()
os.system("makeinstaller.bat")
print("\n====================================\n")
print("\nFile generated (anydown.exe). Cleaning...")
time.sleep(2)
os.remove("files.7z")
os.remove("data\\chatid.dat")
print("\nDone! Press enter to exit!")
input()
