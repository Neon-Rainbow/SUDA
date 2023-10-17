package data;

import java.math.BigDecimal;

public class recorddata {
    private String cardNumber;
    private String type;
    private BigDecimal amount;
    private String location;
    public recorddata(String cardNumber, String type, BigDecimal amount, String location){
        this.cardNumber = cardNumber;
        this.type = type;
        this.amount = amount;
        this.location = location;
    }
    public String getCardNumber(){
        return cardNumber;
    }
    public String getType(){
        return type;
    }
    public BigDecimal getAmount(){
        return amount;
    }
    public String getLocation(){
        return location;
    }
}
