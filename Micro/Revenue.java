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
     */
    public void getEquation() {
        System.out.println("\'Revenue\' = \'price\' x \'quantity\'");
    }

    /**
     * Outputs the full equation represented by this
     */
    public void filledEq() {
        System.out.println(this.revenue + " = " + this.price + " x " + this.quantity);
    }

    /**
     * @param p double representing the given price
     * @modifies this.price
     */
    public void changePrice(double p) {
        this.price = p;
    }

    /**
     * @param q double representing the given quantity
     * @modifies this.quantity
     */
    public void changeQuantity(double q) {
        this.quantity = q;
    }
}
