#ifndef _interestRate_
#define _interestRate_

class interestRateProblem {
    public:
        // Constructors
        interestRateProblem();

        // Accessors
        int getPV() const;
        int getFV() const;
        int getCouponPrice() const;
        int getInterestRate() const;
        int getYears() const;

        // Modifiers
        void setPV();
        void setFV();
        void setCouponPrice();
        void setInterestRate();
        void setYears();

    private:
        // Representation
        int PV;
        int FV;
        int couponPrice;
        int interestRate;
        int years;
};

#endif