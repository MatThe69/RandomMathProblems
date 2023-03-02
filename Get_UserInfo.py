#Imports
from asyncore import read
from base64 import decode
import base64
from distutils.log import error
from getpass import getpass
from imghdr import what
from logging import exception
import re
from site import getusersitepackages
import time
from token import ENCODING
from xml.etree.ElementTree import fromstring
from cryptography.fernet import Fernet
#------------------------------------------------------------------------------------------------------------------------------------
#Generating and Reading the Key
def load_key():
    try:
        with open("key.key", "rb") as g:
            read = g.read()
            return read
    except:
        with open("key.key", "wb") as f:
            GetNewkey = Fernet.generate_key();
            newKey = f.write(GetNewkey)
            return GetNewkey

key = load_key()
fernets = Fernet(key)

#------------------------------------------------------------------------------------------------------------------------------------

#Varibales
usernames = []
passwords = []
loggedIn = False
currentUser = ""

#Functions

#--- register
def register():
    if loggedIn == False:
        getUsername = input("choose your username: ")
        GetPassword = getpass("choose your password: ")

        if (getUsername == "" or GetPassword == ""):
            print("Error, Choose another Username or Password")
            signinorlogin()
        else:
                if (getUsername not in usernames ):
                    usernames.append(getUsername)
                    passwords.append(GetPassword)
                    print("Signed up. Log in to proceed.")
                    save_datas(getUsername, GetPassword)  
                    signinorlogin()      
                else:
                    print("Username already taken. Please choose another one.")
                    signinorlogin()
    else:
        print("You already have an account logged in.")

def login():
    global loggedIn
    if (loggedIn == False):  
        username = input("Enter your username:")
        password = getpass("Enter your Password:")
        if username in usernames and password in passwords:
            if (passwords.index(password) == usernames.index(username)):
                print("Welcome to console, "+ username)
                loggedIn = True
                global currentUser
                currentUser = username
                return 
            else:
                print("Usernae or Password incorrect! Try again.")
                signinorlogin()
        else:
            print("Username or Password incorrect! Try again.")
            signinorlogin()
    else:
        print("You already have an account logged in.")

def SignOutUser():
    global loggedIn
    if (loggedIn == True):
        loggedIn = False
        global currentUser
        currentUser = ""
        print("Logged out.")
    else:
        print("You are not logged in.")


#-- -------------------------------------------------- Saving and loading data-------------------------------------------------------
def save_datas(getUsername, GetPassword):
    my_new_UserNames = bytes(getUsername, 'utf-8')
    my_new_Passes =  bytes(GetPassword, 'utf-8')
    my_new_Passes_Encrypted = fernets.encrypt(my_new_Passes)
    with open("passwords.txt", "a") as f:
        writePass = f.write(((str(my_new_Passes_Encrypted.decode("utf-8")))+"\n"))
        my_new_Users_Encrypted = fernets.encrypt(my_new_UserNames)
    with open("usernames.txt", "a") as g:
        writeUser = g.write(str(my_new_Users_Encrypted.decode("utf-8"))+"\n")
    load_datas()

def load_datas():
    usernames.clear()
    passwords.clear()
    thingtoDecode=[]
    try:
        with open('usernames.txt', 'rb') as f:
            readList = f.read().split(b"\r\n")
            for things in readList:
                try:
                    thingtoDecode = things.decode("utf-8")
                    current = fernets.decrypt(things.decode("utf-8"))
                    usernames.append(current.decode("utf-8"))
                except:
                    print("")
        with open('passwords.txt', 'rb') as f:
            readList = f.read().split(b"\r\n")
            for things in readList:
                try:
                    thingtoDecode = things.decode("utf-8")
                    current = fernets.decrypt(things.decode("utf-8"))
                    passwords.append(current.decode("utf-8"))
                except:
                    print("")
    except:
        print("No Data Found!")
        return
        
def printUserDataForAdmin():
    if currentUser == ("NIGHT_C0DE"):
        printUserNames=[]
        printPasswords = []
        try:
            with open('usernames.txt', 'rb') as f:
                readList = f.read().split(b"\r\n")
                for things in readList:
                    try:
                        thingtoDecode = things.decode("utf-8")
                        current = fernets.decrypt(things.decode("utf-8"))
                        printUserNames.append(current.decode("utf-8"))
                    except:
                        print("")
            with open('passwords.txt', 'rb') as f:
                readList = f.read().split(b"\r\n")
                printPasswords = readList
        except:
            print("No Data Found!")
            return
        print(printUserNames)
        print(printPasswords)
    else:
        print("Error 1")

def deleteUserData():
    if currentUser == ("NIGHT_C0DE"):
        try:
            with open('usernames.txt', 'wb') as f:
                f.write(b"")
            with open('passwords.txt', 'wb') as g:
                g.write(b"")
        except Exception as ex:
            print("Possible error: ", ex)
            return
        print("All data deleted!")
    else:
        print("Error 1")

#-----------------------------------------------------------------------------------------------------------------------------------

#--- Options
def signinorlogin():
    load_datas()
    print("------------------------------------------------------------------------------------")
    print("choose:  a)Sign Up     b)Login    c)quit ")
    account_ans = input("Choose: ")
    if account_ans == "a":
        register()
    if account_ans == "b":
        login()
    if account_ans == "c":
        print("Quitting Accounts...")
        time.sleep(0.2)
signinorlogin()