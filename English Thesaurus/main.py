# This App output shows the definition of a given word. 
#
# Author  David Almog
# Version 1.0
# Since   2020

import json
import sys
import os
import difflib

 
def main():
    if (os.path.exists("data.json")):
        data = json.load(open("data.json"))  
        printOutput("start")
        while True:
            userInput = input("\nEnter word: ").strip().lower() # Input
            if userInput == "bye":
                printOutput("bye") # exit screen
                break
            elif userInput in data:
                out = str (data[userInput])
                print("\n",out[1:len(out)-1]) # printing the definition
            elif userInput =="?":
                printOutput("menu") # menu screen
            else:
                printOutput("other") # Error/ unknown word screen
                if len(difflib.get_close_matches(userInput,data.keys())) > 0:
                    print("\nDid you mean: %s \n" % difflib.get_close_matches(userInput,data.keys())[0])
        print("\n")
    else:
        print("\n - Error - \n")
        exit(1)
    exit(0)

def printOutput(opcode):
    if opcode == "menu":
        print("\n############## Help Manu ##############\n"
            ,"\nTo get the definition of a word"
            ,"\nWrite the Word and click enter"
            ,"\nTo finish the Program Write \'bye\'\n"
            ,"\n#######################################")
    elif opcode == "bye":
        print("\nClose the App ")
        rows = 14
        print("*" * rows, end="\n")
        i = (rows // 2) - 1
        j = 2
        while i != 0:
            while j <= (rows - 2):
                print("*" * i, end="")
                print("_" * j, end="")
                print("*" * i, end="\n")
                i = i - 1
                j = j + 2
    elif opcode == "start":
        print("\n______________________________________\n"
            ,"\nWelcome to word to definition App"
            ,"\n______________________________________\n"
            ,"\nTo view Instructions Enter: \'?\' \n")
    else:
        print("\nUnknown Word... Please try again")
        
main() 

           