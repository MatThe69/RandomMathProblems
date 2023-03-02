# IMPORT ALL MATH FUNCTIONS
from Math_Level_1 import RandomQuestion

def getLevel():
    z = input("Choose 1, 2 or 3.: ")
    match z:
        case "1":
            RandomQuestion()
        case  "2":
            print("PLAY MATH 2")
        case "3":
            print("PLAY MATH 3")

def MathGameintro():
    print("Welcome to Math!")
    print("There are three levels.")
    print("1: Basic Math.")
    print("2: Equasions.")
    print("3: Quadratic Equasions.")
    getLevel()
