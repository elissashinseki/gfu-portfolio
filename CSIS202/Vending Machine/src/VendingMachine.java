import java.awt.Container;

import java.awt.GridLayout;
import java.awt.FlowLayout;
import java.awt.BorderLayout;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;

import javax.swing.JLabel;
import javax.swing.ImageIcon;

import java.awt.Color;

public class VendingMachine extends JFrame
{
    private static final int START_STATE = 1;
    private static final int VEND_STATE = 2;
    
    private static final double QUARTER_VALUE = 0.25;
    private static final double DOLLAR_VALUE = 1.00;
    
    private static final long serialVersionUID = 1L;
    
    private final JButton _aButton;
    private final JButton _bButton;
    private final JButton _cButton;
    private final JButton _dButton;
    private final JButton _eButton; 
    private final JButton _quarterButton;
    private final JButton _dollarButton;
    private final JButton _coinReturn;
    
    private final JTextArea _display;
    private final JTextArea _coinReturnChute;
    private final JTextArea _sodaChute;
    
    private VendingBank _bank;
    private Soda[] _soda;
    private int _choice;
    private int _state;
    private double _topPrice;
    
    
    /**
     * Constructor for the vending machine.
     */
    public VendingMachine()
    {
        final int FRAME_WIDTH = 480;
        final int FRAME_HEIGHT = 620;
        
        JPanel displayPanel;
        JPanel moneyButtonPanel;
        JPanel sodaButtonPanel;
        
        Container contentPane;        
        ImageIcon image = new ImageIcon("src/Coca-Cola.jpg");
        JLabel imageLabel = new JLabel(image);      
        Color bgColor = new Color(210, 33, 5);
        
        // CREATES BANK AND SODA
        _bank = new VendingBank(20);
        _choice = 0;
        _soda = new Soda[5];
        
        _soda[0] = new Soda("Coke", 10, 1.50);
        _soda[1] = new Soda("Cherry Coke", 10, 1.50);
        _soda[2] = new Soda("Sprite", 10, 1.75);
        _soda[3] = new Soda("Dr. Pepper", 10, 1.75);
        _soda[4] = new Soda("Dasani", 10, 1.00);
        
        _topPrice = getTopPrice();       
        
        // WINDOW SETTINGS
        getContentPane().setBackground(bgColor);        
        setSize(FRAME_WIDTH, FRAME_HEIGHT);
        setResizable(false);       
        addWindowListener(new WindowCloser());
        
        // DISPLAYS
        _display = new JTextArea(4, 10);
        _coinReturnChute = new JTextArea(4, 10);
        _sodaChute = new JTextArea(4, 10);
        
        // MONEY AND COIN RETURN BUTTONS
        _coinReturn = new JButton("Coin Return");
        _coinReturn.addActionListener(new coinReturnListener());

        _quarterButton = new JButton("Quarter");
        _quarterButton.addActionListener(new quarterButtonListener());
        
        _dollarButton = new JButton("Dollar");
        _dollarButton.addActionListener(new dollarButtonListener());
             
        // SODA TYPE BUTTONS
        _aButton = new JButton("" + _soda[0].getName());
        _aButton.addActionListener(new AButtonListener());
        
        _bButton = new JButton("" + _soda[1].getName());
        _bButton.addActionListener(new BButtonListener());
        
        _cButton = new JButton("" + _soda[2].getName());
        _cButton.addActionListener(new CButtonListener());
        
        _dButton = new JButton("" + _soda[3].getName());
        _dButton.addActionListener(new DButtonListener());
        
        _eButton = new JButton("" + _soda[4].getName());
        _eButton.addActionListener(new EButtonListener());
        
        // Add components to display panel
        displayPanel = new JPanel();
        displayPanel.setLayout(new BorderLayout());
        displayPanel.add(imageLabel, BorderLayout.CENTER);
        displayPanel.add(_sodaChute, BorderLayout.SOUTH);
        
        // Add components to money button panel
        moneyButtonPanel = new JPanel();
        moneyButtonPanel.setLayout(new GridLayout(5,1));
        moneyButtonPanel.add(_display);
        moneyButtonPanel.add(_quarterButton);
        moneyButtonPanel.add(_dollarButton);
        moneyButtonPanel.add(_coinReturn);
        moneyButtonPanel.add(_coinReturnChute);
        
        // Add components to soda button panel
        sodaButtonPanel = new JPanel();
        sodaButtonPanel.setLayout(new GridLayout(5,1));
        sodaButtonPanel.add(_aButton);
        sodaButtonPanel.add(_bButton);
        sodaButtonPanel.add(_cButton);
        sodaButtonPanel.add(_dButton);
        sodaButtonPanel.add(_eButton);
        
        // Add components to content pane
        contentPane = getContentPane();
        contentPane.setLayout(new FlowLayout());
        contentPane.add(displayPanel);
        contentPane.add(moneyButtonPanel);
        contentPane.add(sodaButtonPanel);        
        
        setState(START_STATE);       
        setVisible(true);
    }
    
    
    /**
     * Resets the vending machine state.
     */
    public void setState(int newState)
    {
        _state = newState;
    }
    
    
    /**
     * Collects money as long as there is not enough change to buy a soda.
     * 
     * @param double - value
     */
    public void moneyManager(double value)
    {
        double topPrice = _topPrice;
        
        _sodaChute.setText("");
        
        if (!_bank.changeEnough(topPrice))
        {
            _bank.collectMoney(value);
            _coinReturnChute.setText("");
        }
        else
        {
            _coinReturnChute.setText(String.format("$%.2f returned", value));
        }
        
        _display.setText(String.format("$%.2f", _bank.getAmountCollected()));
    }
    
    
    /**
     * Sets actions for soda buttons when state is at the start state and the
     * vend state.
     */
    public void sodaButtonAction()
    {
        _coinReturnChute.setText("");
        _sodaChute.setText("");
        
        if (!_soda[_choice].isSoldOut())
        {       
            if (_bank.changeEnough(_soda[_choice].getPrice()))
            {
                setState(VEND_STATE);
                _coinReturnChute.setText("");
            }
            
            // Displays soda price if in start state.
            if (_state == START_STATE)
            {
                _display.setText(String.format("PRICE: $%.2f", _soda[_choice].getPrice()));   
            }
            
            // Vends soda if in vend state.
            else if (_state == VEND_STATE)
            {
                _soda[_choice].vendSoda();
                _sodaChute.setText("You've got a " + _soda[_choice].getName() + "!!");
                _bank.storeMoney(_soda[_choice].getPrice());
                _coinReturnChute.setText(String.format("$%.2f returned", _bank.releaseChange()));
                _display.setText(String.format("$%.2f", _bank.getAmountCollected()));
                    
                setState(START_STATE);
            }
        }
        // Displays that a soda is sold out if there are no more soda cans in the machine
        else
        {
            _display.setText("SOLD OUT");
        }
    }
    
    
    /**
     * Finds and returns the top price of the soda types in the machine.
     * 
     * @return double - top price
     */
    public double getTopPrice()
    {
        double price;
        double topPrice = _soda[0].getPrice();
        
        for (int i = 0; i < _soda.length; i++)
        {
            price = _soda[i].getPrice();
            
            if (topPrice <= price)
            {
                topPrice = _soda[i].getPrice();
            }
        }
        
        return topPrice;
    }
    
    
    /**
     * Selects the soda to have an action placed on.
     */
    private class AButtonListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {
            _choice = 0;
            sodaButtonAction();
        }
    }
    
    
    /**
     * Selects the soda to have an action placed on.
     */
    private class BButtonListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {
            _choice = 1;
            sodaButtonAction();
        }
    }
    
    
    /**
     * Selects the soda to have an action placed on.
     */
    private class CButtonListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {
            _choice = 2;
            sodaButtonAction();
        }
    }
    
    
    /**
     * Selects the soda to have an action placed on.
     */
    private class DButtonListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {
            _choice = 3;
            sodaButtonAction();
        }
    }
    
    
    /**
     * Selects the soda to have an action placed on.
     */
    private class EButtonListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {
            _choice = 4;
            sodaButtonAction();
        }
    }

    
    /**
     * Creates a listener for when users want to add a quarter.
     */
    private class quarterButtonListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {   
            moneyManager(QUARTER_VALUE);
        }
    }
    
    
    /**
     * Creates a listener for when users want to add a dollar.
     */
    private class dollarButtonListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {
            moneyManager(DOLLAR_VALUE);
        }
    }
    
    
    /**
     * Creates a listener for when users want to have their money returned.
     */
    private class coinReturnListener implements ActionListener
    {
        public void actionPerformed(final ActionEvent event)
        {   
            _display.setText("$0.00");
            _coinReturnChute.setText(String.format("$%.2f returned", _bank.releaseChange()));
            setState(START_STATE);
        }
    }
    
    
    /**
     * Allows the window to be closed.
     */
    private class WindowCloser extends WindowAdapter
    {
        public void windowClosing(final WindowEvent event)
        {
            System.exit(0);
        }
    }
}
