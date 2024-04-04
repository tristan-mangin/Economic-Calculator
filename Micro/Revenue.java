package Micro;

/**
 * A class used to solve micro economic problems relating to revenue 
 */
public class Revenue extends MicroProblem implements InnerMicroProblem {
    double price;
    double quantity;
    double revenue;

    /**
     * @effects Constructs new Revenue object with price, quantity and revenue = 0
     */
    public Revenue() {
        this.price = 0;
        this.quantity = 0;
        this.revenue = 0;
    }

    /**
     * @param p double representing the given price
     * @param q double representing the given quantity
     * @effects Constructs new Revenue object with 'p' and 'q' as attributes
     */
    public Revenue(double p, double q) {
        this.price = p;
        this.quantity = q;
        this.revenue = p * q;
    }

    /**
     * Outputs basic equation to solve Revenue related problems
     * 
     * @return output equation
     */
    public String getEquation() {
        String out = "\'Revenue\' = \'price\' x \'quantity\'";
        System.out.println(out);
        return out;
    }

    /**
     * Outputs the full equation represented by this
     * 
     * @return output equation
     */
    public String filledEq() {
        String out = this.revenue + " = " + this.price + " x " + this.quantity;
        System.out.println(out);
        return out;
    }

    /**
     * @return price
     */
    public double getPrice() {
        return this.price;
    }

    /**
     * @return quantity
     */
    public double getQuantity() {
        return this.quantity;
    }
    
    /**
     * @return revenue
     */
    public double getRevenue() {
        return this.revenue;
    }

    /**
     * @param p double representing the given price
     * @modifies this.price
     */
    public void changePrice(double p) {
        this.price = p;
        this.revenue = this.price * this.quantity;
    }

    /**
     * @param q double representing the given quantity
     * @modifies this.quantity
     */
    public void changeQuantity(double q) {
        this.quantity = q;
        this.revenue = this.price * this.quantity;
    }

    /**
     * @effects sets all attributes of this to 0
     */
    public void clear() {
        this.price = 0;
        this.quantity = 0;
        this.revenue = 0;
    }
}
