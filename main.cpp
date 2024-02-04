#include <iostream>
#include <vector>
#include <string>
#include "interestRate.h"

using namespace std;

string COMMANDS[] = {"help", "exit", "ci", "di", "pv", "ytm"};

// Outputs Instructions and the list of commands to the terminal
void help() {
    cout << "\t1. exit\t- terminate the program\n" <<
    "\t2. ci\t- solve for compounding interest\n" <<
    "\t3. di\t- solve for discounting interest\n" <<
    "\t4. pv\t- solve for present value\n" <<
    "\t5. ytm\t- solve for yield to maturity\n"<< endl;
}

void compoundInterest() {}

void discountInterest() {}

void presentValue() {} 

void yieldMaturity() {}

// main function of the program handles user input and direction
int main() {
    string topic = "";
    bool exit = false;
    cout << "Welcome to the Economic Calculator!\n\nHow can I help you today?\n" << endl;

    // main loop of the program prompts user until they want to exit
    while (!exit) {
        cout << ">> ";
        cin >> topic;
        
        if (topic == "help" || topic == "Help" || topic == "HELP") { help(); }
        else if (topic == "exit") { exit = true; }
        else if (topic == "ci") {}
        else if (topic == "di") {}
        else if (topic == "pv") {}
        else if (topic == "ytm") {}
        else { cout << "Please use one of the valid commands\ntype 'help' for full list of commands\n" << endl; }
    }

    return 0;
}