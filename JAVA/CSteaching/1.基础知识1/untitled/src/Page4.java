public class Page4 {
    public static void func1(){
        double money = 0;
        final double rate = 0.00417;
        for(int i = 1; i <= 6; i++){
            money = (100 + money)*(1 + rate);
        }
        System.out.println(money);
    }

    public static void main(String[] args){
        System.out.println("question1:");
        func1();
        System.out.println();
    }
}
