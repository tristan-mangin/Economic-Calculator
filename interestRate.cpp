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

// Modifiers
void interestRateProblem::setPV(float x) { PV = x; }
void interestRateProblem::setFV(float x) { FV = x; }
void interestRateProblem::setCouponRate(float x) { couponRate = x; }
void interestRateProblem::setInterestRate(float x) { interestRate = x; }
void interestRateProblem::setYears(float x) { years = x; }

// Solvers