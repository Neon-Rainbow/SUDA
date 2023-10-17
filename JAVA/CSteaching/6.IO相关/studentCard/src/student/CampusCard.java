package student;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class CampusCard {
    private String cardNumber; //10位卡号
    private BigDecimal balance; //余额
    private BigDecimal totalConsumption = BigDecimal.valueOf(0); //总消费
    private BigDecimal totalSave = BigDecimal.valueOf(0);
    private List<Consumption> consumptionList = new ArrayList<>();
    public CampusCard(String cardID){
        this.cardNumber = cardID;
        this.balance = BigDecimal.valueOf(0);
    }

    public String getCardNumber(){
        return cardNumber;
    }

    public BigDecimal getBalance(){
        return balance;
    }

    public BigDecimal getTotalConsumption(){
        return totalConsumption;
    }

    public BigDecimal getTotalSave(){
        return totalSave;
    }

    public List<Consumption> getConsumption(){
        return consumptionList;
    }

    public void addBalance(BigDecimal amount){
        balance = balance.add(amount);
        totalSave = totalSave.add(amount);
    }
    public void consume(BigDecimal amount){
        balance = balance.subtract(amount);
        totalConsumption = totalConsumption.add(amount);
    }

    public void addConsumption(Consumption consumption){
        consumptionList.add(consumption);
    }
}
