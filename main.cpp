#include <iostream>
#include <vector>
#include <string>

using namespace std;
/*
TOPICS TO INCLUDE
    Interest Rates
    Monetary Policy
    Fiscal Policy
*/
void interestRates() {}

void monetaryPolicy() {}

void fiscalPolicy() {}

// main function of the program handles user input and direction
int main() {
    string topic = "";
    int topicNum = -1;
    bool exit = false;
    cout << "Welcome to the Economic Calculator!\n\nWhat topic can I help you with today?" << endl;

    // main loop of the program prompts user until they want to exit
    while (!exit) {
        cout << "1. Interest Rates\n2. Monetary Policy\n3. Fiscal Policy\n0. Exit\n\n>>";
        cin >> topic;

        // Make sure the input is valid
        if (isalpha(topic[0])) { 
            cout << "\nPlease Select a valid topic\n";
            continue;
        }
        topicNum = stoi(topic);

        // Checks prompt and goes to appropriate method
        if (topicNum == 0) { exit = true; }
        else if (topicNum == 1) { interestRates(); }
        else if (topicNum == 1) { monetaryPolicy(); }
        else if (topicNum == 1) { fiscalPolicy(); }
        else {
            cout << "\nPlease Select a valid topic\n\n";
        }
    }



    return 0;
}