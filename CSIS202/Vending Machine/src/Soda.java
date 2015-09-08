
public class Soda
{
    // instance variables
    private String _name;
    private int _count;
    private double _price;
    
    /**
     * Constructor for a soda type.
     * 
     * @param String - name
     * @param int - count
     */
    public Soda(String name, int count, double price)
    {
        _name = name;
        _count = count;
        _price = price;
    }
    
    
    /**
     * Adds soda to the count.
     * 
     * @param count
     */
    public void addSoda(int count)
    {
        _count += count;
    }
    
    
    /**
     * Subtracts 1 soda from the count.
     */
    public void vendSoda()
    {
        _count -= 1;
    }
    
    
    /**
     * Returns the name of the soda.
     * 
     * @return String - name
     */
    public String getName()
    {
        return _name;
    }
  
    
    /**
     * Returns the price of the soda.
     * 
     * @return double - price
     */
    public double getPrice()
    {
        return _price;
    }
    
    
    /**
     * Returns whether soda is sold out or not.
     * 
     * @return boolean - soldOut
     */
    public boolean isSoldOut()
    {
        return (_count == 0);
    }
}
