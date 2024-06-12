#include "interestRate.h"

// Constructor
interestRateProblem::interestRateProblem() {
    PV = std::nan("0");
    FV = std::nan("0");
    couponRate = std::nan("0");
    interestRate = std::nan("0");
    years = std::nan("0");
}

// Accessors
float interestRateProblem::getPV() const { return PV; }
float interestRateProblem::getFV() const { return FV; }
float interestRateProblem::getCouponRate() const { return couponRate; }
float interestRateProblem::getInterestRate() const { return interestRate; }
float interestRateProblem::getYears() const { return years; }

// Float input modifiers
void interestRateProblem::setPV(float x) { PV = x; }
void interestRateProblem::setFV(float x) { FV = x; }
void interestRateProblem::setCouponRate(float x) { couponRate = x; }
void interestRateProblem::setInterestRate(float x) { interestRate = x; }
void interestRateProblem::setYears(float x) { years = x; }

// String input modifiers
void interestRateProblem::setPV(string x) { PV = stof(x); }
void interestRateProblem::setYears(string x) { years = stof(x); }
void interestRateProblem::setFV(string x) { FV = stof(x); }
void interestRateProblem::setInterestRate(string x) { interestRate = stof(x); }
void interestRateProblem::setCouponRate(string x) { couponRate = stof(x); }

// Solvers

// Discounting 
float interestRateProblem::solvePV() {
    float numerator = FV;
    float denominator = pow(1 + interestRate, years);
    return numerator / denominator;
}

// Compounding
float interestRateProblem::solveFV() {
    return PV * pow(1 + interestRate, years);
}

// Solve for price of coupon bond
float interestRateProblem::solveCouponRate() {
    float result = 0;
    float numerator = couponRate * FV;
    float denominator;

    for (unsigned int i = 1; i <= years; i++) {
        denominator = pow(1 + interestRate, i);
        result += numerator / denominator;
    }

    numerator = FV;
    result += numerator / denominator;
    return result;
}

// Solve for yield to maturity
float interestRateProblem::solveYTM() {
    float result = FV / PV - 1;
    
    if (result == interestRate) { 
        return result; 
    }
    else { 
        interestRate = result; 
        return result;
    }
}