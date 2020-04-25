version = 1.0

import os
import time
import sys
import math
import os.path
import urllib
import urllib.request
import pip

try:
    import requests
except:
    try:
        version = os.system("pip --version")
        sys.stdout.write("py -m pip install requests")
        import requests
    except:
        sys.stdout.write("python -m pip install -U pip")
        sys.stdout.write("py -m pip install requests")
        import requests

prefix = "§8» §3PandaAPI §8| §9"

#
# ┌────────────────────────────────────────────────────────────────────────────┐
# │                                                                            │
# │ IIIII  IIII   IIIII  IIIII  IIIII        IIII   IIIII  IIIII  IIII   IIIII │
# │ I      I   I  I      I      I   I        I   I  I   I  I   I  I   I  I   I │
# │ I  II  IIII   IIIII  IIIII  I   I        IIII   IIIII  I   I  I   I  IIIII │
# │ I   I  I I    I      I      I   I        I      I   I  I   I  I   I  I   I │
# │ IIIII  I  I   IIIII  IIIII  I   I IIIII  I      I   I  I   I  IIII   I   I │
# │                                                                            │
# └────────────────────────────────────────────────────────────────────────────┘
#
# Functions:
#
# delayedText
#   - Displays a Text and delays the following action by a given value
# colorText
#   - Colors a text
# betterText
#   - Displays a Text that can contain color codes
# betterInput
#   - Creates a input field using a given text that can contain color codes
# stateText
#   - Prints a Basetext and cicles through different given States with a given delay
# question
#   - Displays a Question with a given title and given answers. Returns one of the answers or nothing if the answer given was incorrect
# getPlatform
#   - Returns the name of the Platform that the Programm is run on
# clearScreen
#   - Clears the screen on every Platform
# goToLastLine
#   - Moves the cursor to the last written line
# progressBar
#   - Displays a Progressbar with a given with and percentage and gives it a given color
# createDirectory
#   - Creates a Directory at a given path
# writeLine
#   - Adds a given Text as a new Line to a given File
# readLine
#   - Returns a given line of a given File
# getFileContent
#   - Returns a list of all Written lines in a given File
# fileExists
#   - Returns if a File exists or not 
# clearFile
#   - Clears the content of a File
# commandInput
#   - Creates an Input field for registered Commands
# registerCommand
#   - Registers a Command for the Command Handler
# prefixBuilder
#   - Creates a console Prefix
#

commands = []
executors = []
descriptions = []

COLORS = {\
"0" : "\033[0;30;47m", # (Black)
"1" : "\033[1;31;40m", # (Bright Red)
"2" : "\033[1;34;40m", # (Bright Blue)
"3" : "\033[1;32;40m", # (Bright Green)
"4" : "\033[1;35;40m", # (Bright Magenta)
"5" : "\033[1;36;40m", # (Bright Cyan)
"6" : "\033[0;37;40m", # (Light Grey)
"8" : "\033[1;30;40m", # (Dark Gray)
"9" : "\033[1;37;40m", # (White)
"a":"\u001b[40m",      # (Black Background)
"b":"\u001b[43m",      # (Yellow Background)
"c":"\u001b[46;1m",    # (Cyan Background)
"d":"\033[0;35;47m",   # (Magenta Background)
}

# Displays a Text and delays the following action by a given value
def delayedText(text, delay):
    betterText(text)
    time.sleep(delay)

# Colors a text
def colorText(text):
    for color in COLORS:
        text = text.replace("§" + color, COLORS[color])
    return text

# Displays a Text that can contain color codes
def betterText(text, end="\n"):
    print(colorText(text + "§9"), end=end)

# Creates a input field using a given text that can contain color codes
def betterInput(text):
    betterText(text, end=" ")
    back = input()
    return back

# Prints a Basetext and cicles through different given States with a given delay
def stateText(basetext, states, delay):
    betterText(" ")
    i = 0
    while i < len(states):
        goToLastLine()
        betterText(basetext + states[i])
        time.sleep(delay)
        i += 1

# Displays a Question with a given title and given answers
# Returns one of the answers or nothing if the answer given was incorrect
def question(title, answers):
    betterText(title)
    i = 0
    while i < len(answers):
        betterText(chr(97+i) + ") " + answers[i])
        i += 1
    answer = input("Answer: ")
    try:
        if answer in answers:
            return answer
        elif ord(answer) < (97 + len(answers)):
            return answers[ord(answer)-97]
    except:
        return answer

# Returns the name of the Platform that the Programm is run on
def getPlatform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

# Clears the screen on every Platform
def clearScreen():
    platform = getPlatform()
    if(platform == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

# Moves the cursor to the last written line
def goToLastLine():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)

# Displays a Progressbar with a given with and percentage and gives it a given color
def progressBar(percent, width=10, color="3", default="6"):
    clearScreen()
    slots = math.floor(width * (percent/100))
    text=""
    i = 0
    while i < width:
        if i < slots:
            text = text + "§" + str(color) + "█"
        else:
            text = text + "§9█"
        i +=1
    return text + " §9" + str(slots) + "/" + str(width)

# Creates a Directory at a given path
def createDirectory(path):
    if not os.path.exists(path):
        os.mkdir(path)

# Adds a given Text as a new Line to a given File
def writeLine(directory, text):
    file = open(directory, "a+")
    file.write(text + "\n")
    file.close()

# Returns a given line of a given File
def readLine(directory, line):
    file = open(directory, "r")
    lines = file.readlines()
    if len(lines) > line:
        return lines[line].replace("\n", "")
    else:
        return "null"

# Returns a list of all Written lines in a given File
def getFileContent(directory):
    file = open(directory, "r")
    contents = file.readlines()
    i = 0
    while i < len(contents):
        contents[i] = contents[i].replace("\n", "")
        i += 1
    return contents

# Returns if a File exists or not  
def fileExists(directory):
    if os.path.isfile(directory):
        return True
    else:
        return False

# Clears the content of a File
def clearFile(directory):
    file = open(directory, 'r+')
    file.truncate(0)
    file.close()

# Creates an Input field for registered Commands
def commandInput(prefix):
    args = betterInput(prefix).split(" ")
    cmd = args[0]
    args.remove(cmd)
    if args == None:
        args = [""]
    if cmd in commands:
        index = commands.index(cmd)
        try:
            executors[index](args, prefix)
        except:
            betterText(prefix + "§1Input Error!")
            commandInput(prefix)
    else:
        betterText(prefix + "§1Unknown Command!")
        commandInput(prefix)
        
# Registers a Command for the Command Handler
def registerCommand(command, executor, description=""):
    commands.append("/" + command)
    executors.append(executor)
    descriptions.append(description)

# Creates a console Prefix
def prefixBuilder(prefix, textcolor="9", charactercolor="8"):
    back = "§" + str(charactercolor) + "» §" + str(textcolor) + str(prefix) + "§" + str(charactercolor) + " | §9"
    return back

def pandaapiCommand(msg, sentprefix):
        if msg[0] == "list" or msg[0] == "help":
            betterText("")
            betterText(prefix + "§8────────────────────────────§3Commands§8────────────────────────────")
            for command in commands:
                if descriptions[commands.index(command)] != "":
                    betterText(prefix + "§3" + command + "§8 - §3" + descriptions[commands.index(command)])
                else:
                    betterText(prefix + "§3" + command)
            betterText(prefix + "§8────────────────────────────§3Commands§8────────────────────────────")
            betterText("")
            commandInput(sentprefix)
        if msg[0] == "info":
            betterText("")
            betterText(prefix + "§8────────────────────────────§3PandaAPI§8────────────────────────────")
            betterText(prefix + "§3PandaAPI")
            betterText(prefix + "§3version: §8" + str(version))
            betterText(prefix + "§3Author: Green_Panda")
            betterText(prefix + "§8────────────────────────────§3PandaAPI§8────────────────────────────")
            betterText("")
            commandInput(sentprefix)
        else:
            betterText(prefix + "§1Unknown Command!")

def checkVersion():
    global version
    vFile = requests.get("https://github.com/GreenP4nda/PandaAPI/raw/master/PandaAPI.py")
    content = vFile.text.split("\n")
    v = float(content[0].replace("version = ", ""))
    if(v > version):
        update()

def update():
    betterText(prefix+ "§3There is a new Update for §5PandaAPI.")
    answer = question(prefix + "§3Do you want do update to the new Version?", ["Yes", "No"])
    if answer == "Yes":
        vFile = requests.get("https://github.com/GreenP4nda/PandaAPI/raw/master/PandaAPI.py")
        content = vFile.text.split("\n")
        v = float(content[0].replace("version = ", ""))
        betterText(prefix + "§3Downloading §5" + str(v) + " §3Version of §5PandaAPI.")
        open("PandaAPI.py", "wb").write(vFile.content)
        betterText(prefix + "§3The new Version has been downloaded. §1Please restart the Project.")
    elif answer == "No":
        betterText(prefix + "Continuing with outdated Version of PandaAPI")
    else:
        betterText("§1Invalid answer!")
        clearScreen()
        update()
            
registerCommand("pandaapi", pandaapiCommand)

clearScreen()

betterText("")
betterText("§3 ┌──────────────────────────────────────────────────────────────┐")
betterText("§3 │                                                              │")
betterText("§3 │  ██████  ██████  ██████  ████    ██████  ██████  ██████  ██  │")
betterText("§3 │  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  │")
betterText("§3 │  ██████  ██████  ██  ██  ██  ██  ██████  ██████  ██████  ██  │")
betterText("§3 │  ██      ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██      ██  │")
betterText("§3 │  ██      ██  ██  ██  ██  ████    ██  ██  ██  ██  ██      ██  │")
betterText("§3 │                                                              │")
betterText("§3 │  By Green_Panda                                              │")
betterText("§3 └──────────────────────────────────────────────────────────────┘")
betterText("§8 Version: " + str(version))

time.sleep(3)
clearScreen()

if not fileExists("Readme.txt"):
    writeLine("README.txt", " ------------------------------------------------------ ")
    writeLine("README.txt", "|                                                      |")
    writeLine("README.txt", "| IIII   IIIII  IIIII  IIII   IIIII    IIIII  IIII   I |")
    writeLine("README.txt", "| I   I  I   I  I   I  I   I  I   I    I   I  I   I  I |")
    writeLine("README.txt", "| IIII   IIIII  I   I  I   I  IIIII    IIIII  IIII   I |")
    writeLine("README.txt", "| I      I   I  I   I  I   I  I   I    I   I  I      I |")
    writeLine("README.txt", "| I      I   I  I   I  IIII   I   I    I   I  I      I |")
    writeLine("README.txt", "|                                                      |")
    writeLine("README.txt", "| by Green_Panda                                       |")
    writeLine("README.txt", " ------------------------------------------------------ ")
    writeLine("README.txt", "Version: " + str(version))
    writeLine("README.txt","")
    writeLine("README.txt", "This Project uses the PandaAPI.")
    writeLine("README.txt", "In order for this Project to function correctly, the PandaAPI must be in the same Folder as the decired Project at all times!")

checkVersion()
input()
