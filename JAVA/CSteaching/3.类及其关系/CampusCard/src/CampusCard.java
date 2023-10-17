import java.util.ArrayList;
import java.util.List;

public class CampusCard {
    private String cardNumber;
    private double balance;
    private List<Consumption> consumptionList = new ArrayList<>();
    public CampusCard(String cardID){
        this.cardNumber = cardID;
        this.balance = 0;
    }

    public String GetCardNumber(){
        return cardNumber;
    }

    public double GetBalance(){
        return balance;
    }

    public List<Consumption> getConsumption(){
        return consumptionList;
    }

    public void AddBalance(double amount){
        balance += amount;
    }


    public void Consume(double amount){
        balance -= amount;
    }

    public void addConsumption(Consumption consumption){
        consumptionList.add(consumption);
    }
}
