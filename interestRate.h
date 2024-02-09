#ifndef _interestRate_
#define _interestRate_

#include <cmath>
#include <string>

using namespace std;

class interestRateProblem {
    public:
        // Constructors
        interestRateProblem();

        // Accessors
        float getPV() const;
        float getFV() const;
        float getCouponRate() const;
        float getInterestRate() const;
        float getYears() const;

        // Float Input Modifiers
        void setPV(float x);
        void setFV(float x);
        void setCouponRate(float x);
        void setInterestRate(float x);
        void setYears(float x);

        // String Input Modifiers
        void setPV(string x);
        void setFV(string x);
        void setCouponRate(string x);
        void setInterestRate(string x);
        void setYears(string x);

        // Solvers
        float solvePV();
        float solveFV();
        float solveCouponRate();
        float solveYTM();
        float solveYears();

    private:
        // Representation
        float PV;
        float FV;
        float couponRate;
        float interestRate;
        float years;
};

#endif