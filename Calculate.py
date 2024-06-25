'''
Created by Tristan Mangin on 6/25/2024

This file will handle all of the user interaction within the program. It will take input
and return results to the terminal based on calculations made in imported classes.
'''

# Outputs a valid list of prompts to the terminal when called
def printHelp():
    print("""List of Valid Prompts: \n
    \thelp \t-\tlist valid prompts 
    \tabout \t-\tlearn more about the program and how it works 
    \tquit \t-\texit the program
    \nPrompts are NOT case sensitive\n""")
    
# Outputs the program information to the terminal when called 
def printInfo():
    print("""\n    ECONOMIC CALCULATOR is a personal project started by TRISTAN MANGIN as a sophomore studying computer science and
    economics at RENSSELAER POLYTECHNIC INSTITUTE.\n
    This project was started as a way to aid in his studies of economic formulas and ideas, as well as an outlet to 
    practice coding and version control software. Because of this it is in continuous development.\n""")

# Main body of the program that will continue to run until the user exits 
def runProgram(running):
    print("Welcome to the Economic Calculator!")
    print("\nPlease enter a prompt. For a list of valid prompts type \'help\'. For more info type \'about\'")

    # Input will be taken from the user
    # Classes and their methods will be called to make calculations
    prompt = ""
    while running:
        prompt = input(">> ").lower().strip()

        if prompt == "help":
            printHelp()
        elif prompt == "about":
            printInfo()
        elif prompt == "quit":
            running = False
            break
        else:
            print("Sorry that is an unknown prompt and/or has not been implemented yet.\n")

if __name__ == "__main__":
    runProgram(True)