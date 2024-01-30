#ifndef _interestRate_
#define _interestRate_

#include <cmath>

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

        // Modifiers
        void setPV(float x);
        void setFV(float x);
        void setCouponRate(float x);
        void setInterestRate(float x);
        void setYears(float x);

        // Solvers
        float solvePV();
        float solveFV();
        float solveCouponRate();
        float solveInterestRate();
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