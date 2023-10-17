public class Consumption {
    private String time;
    private double amount;
    private String location;

    public Consumption(String time, double amount, String location){
        this.time = time;
        this.amount = amount;
        this.location = location;
    }

    public String getTime() {
        return time;
    }

    public double getAmount() {
        return amount;
    }

    public String getLocation() {
        return location;
    }
}
