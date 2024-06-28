'''
Created by Tristan Mangin on 6/25/2024

This file will handle all of the user interaction within the program. It will take input
and return results to the terminal based on calculations made in imported classes.
'''
import Revenue

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

# Gathers information for the revenue problem being solved
def revenueProblem(problems):
    print("What name should we save this problem as?")
    name = input(">> ").lower().strip().split()
    print("Which component of revenue do you want to solve for?\n\t1. Price\n\t2. Quantity\n\t3. Revenue")
    component = input(">> ").lower().strip().split()

    # Gather known componenets
    if "price" in component:
        input1 = input("Quantity = ")
        input2 = input("Revenue = ")
        problems[name] = Revenue(name, component, input1, input2)
        print("Given a quantity of {:.2f} and a revenue of {:.2f}\n...Price = {:.2f}".format(input1, input2, component))
        
    elif "quantity" in component:
        input1 = input("Price = ")
        input2 = input("Revenue = ")
        problems[name] = Revenue(name, component, input1, input2)
        print("Given a price of {:.2f} and a revenue of {:.2f}\n...Quantity = {:.2f}".format(input1, input2, component))

    elif "revenue" in component:
        input1 = input("Price = ")
        input2 = input("Quantity = ")
        problems[name] = Revenue(name, component, input1, input2)
        print("Given a price of {:.2f} and a quantity of {:.2f}\n...Revenue = {:.2f}".format(input1, input2, component))

    else:
        print("I don't recognize that component as a part of revenue. Try a new kind of problem to solve.")

# Check for other input that is not on the valid list of calculations but is still valid
def checkInput(prompt):
    greetings = ["hi", "hello", "howdy", "hola", "hallo"]
    positive = ["good", "great", "grand", "jolly"]
    negative = ["bad", "horrible", "terrible", "awful"]
    valid = False

    if prompt[0] in greetings:
        print("Hello!")
        valid = True
    if prompt[0] in positive:
        print("That's great I'm glad to hear!")
        valid = True
    if prompt[0] in negative:
        print("I'm very sorry to hear that.")
        valid = True
    
    return valid

# Main body of the program that will continue to run until the user exits 
def runProgram(running, problems):
    print("Welcome to the Economic Calculator!")
    print("\nPlease enter a prompt. For a list of valid prompts type \'help\'. For more info type \'about\'")

    # Input will be taken from the user
    # Classes and their methods will be called to make calculations
    prompt = ""
    while running:
        prompt = input(">> ").lower().strip().split()

        if "help" in prompt:
            printHelp()
        elif "about" in prompt:
            printInfo()
        elif "revenue" in prompt:
            revenueProblem(problems)
        elif "quit" in prompt:
            running = False
            break
        else:
            if not checkInput(prompt):
                print("Sorry that is an unknown prompt and/or has not been implemented yet.\n")

if __name__ == "__main__":
    problems = dict()
    runProgram(True, problems)