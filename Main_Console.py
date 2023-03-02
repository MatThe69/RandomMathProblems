# Imports
import os
import time

# Importing other scripts
from Possible_Functions import cmds, functionToCall, functionsFunction
from Get_UserInfo import signinorlogin, printUserDataForAdmin, deleteUserData
from MathMenu import MathGameintro

# Variables
getCmd = True

# STarting
def WelcomeUserUI():
    print("Welcome to NAME.")
    print("Type - help for help")
    print(" ")
WelcomeUserUI();


#----------------------------------------FUNCTIONS------------------------------------------------#
# Functions
def HelpFunction():
    getCommands = cmds
    getFunctionsName = functionsFunction
    res = "\n".join("|{}       \t        {}".format(x, y) for x, y in zip(getCommands, getFunctionsName))
    print("------------------------------------------------------------------------------------------")
    print("Help Menu:")
    print("")
    print("!!Important!!: - is required inorder to execute functions.")
    print("")
    print(res)

def InitMath():
    os.system('cls')
    MathGameintro()


def QuitTheConsole():
    print("Quitting...")
    time.sleep(0.3)
    exit()

def SignUp():
     signinorlogin()

def ClearConsoleFcn():
    os.system('cls')

def printUserDataForAdmin():
    printUserDataForAdmin()

def deleteUserDataForAdmin():
    deleteUserData()

#-------------------------------------------FUNCTIONS-------------------------------------------#




# Recive Commands
def fncCaller(revicedFCN):
    revicedFCN()

# Running the console
while getCmd == True:
    cmd = input("cmd: ")
    cmdSpilit = cmd.split(" ")
    if (cmdSpilit.__len__()==2):
        if (cmdSpilit[1] in cmds and cmdSpilit[0] == "-"):
            fncCaller(locals()[functionToCall[(cmds.index(cmdSpilit[1]))]])
        else:
            print("'"+cmd+"'" + " is not recognized as an internal command.")
    else:
            print("'"+cmd+"'" + " is not recognized as an internal command.")  