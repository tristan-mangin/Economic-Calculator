#include <iostream>
#include <vector>
#include <string>
#include "interestRate.h"

using namespace std;

// Outputs Instructions and the list of commands to the terminal
void help() {
    cout << "\t1. exit\t- terminate the program\n" <<
    "\t2. ci\t- solve for compounding interest\n" <<
    "\t3. di\t- solve for discounting interest\n" <<
    "\t4. pv\t- solve for present value\n" <<
    "\t5. ytm\t- solve for yield to maturity\n" << endl;
}

/*
Collects variables and solves for the missing variable in compounding interest problems
*/
interestRateProblem compoundInterest() {
    string solve;
    bool solving = false;

    cout << "What do you need to solve for?" << endl;

    // Prompts user to choose what to solve for
    while (!solving) {  
        cout <<"\t1. face value\n\t2. present value\n\t3. Yield to Maturity\n>> " << endl;
        cin >> solve;

        if (solve != "1" || solve != "2" || solve != "3") { 
            cout << "please choose a valid number\n" << endl;
        }else { solving = true; }
    }

    interestRateProblem current = interestRateProblem();
    bool haveFV, havePV, haveInt;
    if (solve == "1") { 
        haveFV = false; 
        havePV = true;
        haveInt = true;
    }
    else if (solve == "2") { 
        haveFV = true;
        havePV = false; 
        haveInt = true;
    }
    else { 
        haveFV = true;
        havePV = true;
        haveInt = false; 
    }

    string info;
    float result;
    while (solving) {   
        // Set variables that already exist in the problem
        if (haveFV) {
            cout << "Face Value:" << endl;
            cin >> info;
            current.setFV(info);
        }if (havePV) {
            cout << "Present Value:" << endl;
            cin >> info;
            current.setPV(info);
        }if (haveInt) {
            cout << "Interest Rate:" << endl;
            cin >> info;
            current.setInterestRate(info);
        }
        cout << "Number of Years:" << endl;
        cin >> info;
        current.setYears(info);

        // Solve for last variable
        if (solve == "1") { result = current.solveFV(); }
        else if (solve == "2") { result = current.solvePV(); }
        else { result = current.solveYTM(); }
        solving = false;
    }

    return current;
}

interestRateProblem discountInterest() {}

interestRateProblem presentValue() {} 

interestRateProblem yieldMaturity() {}

// main function of the program handles user input and direction
int main() {
    bool exit = false;
    string topic = "";
    vector<interestRateProblem> solvedIR;

    cout << "Welcome to the Economic Calculator!\n\nHow can I help you today?\n" << endl;

    // main loop of the program prompts user until they want to exit
    while (!exit) {
        cout << ">> ";
        cin >> topic;
        
        if (topic == "help" || topic == "Help" || topic == "HELP") { help(); }
        else if (topic == "exit") { exit = true; }
        else if (topic == "ci") { solvedIR.push_back(compoundInterest()); }
        else if (topic == "di") { solvedIR.push_back(discountInterest()); }
        else if (topic == "pv") { solvedIR.push_back(presentValue()); }
        else if (topic == "ytm") { solvedIR.push_back(yieldMaturity()); }
        else { cout << "Please use one of the valid commands\ntype 'help' for full list of commands\n" << endl; }
    }

    return 0;
}