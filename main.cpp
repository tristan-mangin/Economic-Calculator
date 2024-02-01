#include <iostream>
#include <vector>
#include <string>
#include "interestRate.h"

using namespace std;

string COMMANDS[] = {"help", "exit", "ci", "di", "pv", "ytm"};

/*
Called when the user chooses to solve an interest rate problem
    - Takes user input to choose what is being solved for 
    - Adds variables to a class and performs operations within the class
*/

// Outputs Instructions and the list of commands to the terminal
void help() {
    cout << "Prints instructions and list of commands" << endl;
}

void interestRates() {

}

void monetaryPolicy() {

}

void fiscalPolicy() {
    
}

// main function of the program handles user input and direction
int main() {
    string topic = "";
    bool exit = false;
    cout << "Welcome to the Economic Calculator!\n\nHow can I help you today?" << endl;

    // main loop of the program prompts user until they want to exit
    while (!exit) {
        cout << ">>";
        cin >> topic;
        
        if (topic == "help" || topic == "Help" || topic == "HELP") { help(); }
        else if (topic == "exit") { exit = true; }
    }

    return 0;
}