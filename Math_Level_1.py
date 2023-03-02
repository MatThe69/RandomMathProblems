import math
import random

firstNumber = 0
secondNumber = 0
currentSyntax = "+"
correctAns = 0
possibleSyntax = ["+","-","*","/"]



def printProblem():
    print(firstNumber,currentSyntax,secondNumber)

def getSyntan(z):
    global correctAns
    if z == 0:
        correctAns = firstNumber + secondNumber
        return
    elif z == 1:
        correctAns = firstNumber - secondNumber
        return 
    elif z == 2:
        correctAns = firstNumber * secondNumber
        return
    elif z == 3:
        print("Round it to 2 decimals.")
        correctAns = round(firstNumber/secondNumber, 2)
        return

def RandomQuestion():
    global firstNumber
    global secondNumber
    global currentSyntax
    firstNumber = math.floor(random.random()*1000)
    secondNumber = math.ceil(random.random()*1000)
    SyntaxNumber = math.ceil(random.randint(0,3))
    currentSyntax = possibleSyntax[SyntaxNumber]
    match SyntaxNumber:
        case 0:
            getSyntan(0)
        case 1:
            getSyntan(1)
        case 2:
            getSyntan(2)
        case 3:
            getSyntan(3)
    printProblem()
    ans = input("ANSWER: ")
    if str(ans)==str(correctAns):
        print("Correct!")
    else:
        print("Incorrect! Correct answer: "+str(correctAns))
    
    again=input("Again? y/n: ")
    match again:
        case "y":
            RandomQuestion()
        