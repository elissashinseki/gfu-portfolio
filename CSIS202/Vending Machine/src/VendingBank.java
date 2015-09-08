
public class VendingBank
{   
    private double _amountCollected;
    private double _amountStored;
    
    /**
     * Constructor for the vending machine bank.
     * 
     * @param double - amount
     */
    public VendingBank(double amount)
    {
        _amountStored = amount;
        _amountCollected = 0;
    }
    
    
    /**
     * Collects money into a holding collection.
     * 
     * @param double - amount
     */
    public void collectMoney(double amount)
    {
        _amountCollected += amount;
    }
    
    
    /**
     * Stores the money in a storage area.
     * 
     * @param double - price
     */
    public void storeMoney(double price)
    {
        double amount = price;
        
        _amountCollected -= amount;
        _amountStored += amount;
    }
    
    
    /**
     * Clears and returns the money in the holding collection
     * to be released as change.
     * 
     * @return double - change
     */
    public double releaseChange()
    {
        double change = _amountCollected;
        _amountCollected = 0;
        
        return change;
    }
    
    
    /**
     * Returns the amount collected in the holding collection.
     * 
     * @return double - amount collected
     */
    public double getAmountCollected()
    {
        return _amountCollected;
    }
    
    
    /**
     * Returns amount stored.
     * 
     * @return double - amount stored in bank
     */
    public double getAmountStored()
    {
        return _amountStored;
    }
    
    
    /**
     * Clears the amount in the vending bank.
     */
    public void clearAmountStored()
    {
        _amountStored = 0;
    }
    
    
    /**
     * Returns whether or not money is enough to buy a soda.
     * 
     * @param double - price
     * @return double - change enough
     */
    public boolean changeEnough(double price)
    {       
        return (_amountCollected >= price);
    }
}