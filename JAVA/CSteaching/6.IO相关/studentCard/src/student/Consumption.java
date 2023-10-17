package student;

import java.math.BigDecimal;

public class Consumption {
    //private String time;
    private String type; //用卡类型
    private BigDecimal amount; //发生金额
    private String location; //发生地点编号

    public Consumption(String type, BigDecimal amount, String location){
        //this.time = time;
        this.type = type;
        this.amount = amount;
        this.location = location;
    }

    /*
    public String getTime() {
        return time;
    }
    */
    public String getType(){
        return type;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public String getLocation() {
        return location;
    }
}
