import random

myName = "KPA" #global variable

def dice():
    simDice = random.randint(1,7)
    print(myName+"is rolling the dice")
    return simDice

def sayMyName():
    # myName = "KPA" #local variable
    print("Hello my name is"+myName)

number = dice()
print(number)
sayMyName()
print("My name is"+myName)
