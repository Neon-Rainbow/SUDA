import java.util.Scanner;

public class Page3 {
    public static void func1(){
        //a = (v1 - v0)/t
        Scanner in = new Scanner(System.in);
        System.out.println("输入起始速度v0,单位为m/s");
        int v0 = in.nextInt();
        System.out.println("输入最终速度v1,单位为m/s");
        int v1 = in.nextInt();
        System.out.println("请输入时间,单位为s");
        int t = in.nextInt();
        System.out.println("加速度为" + (v1 - v0)/t + "m/s");
    }

    public static void func2(){
        Scanner in = new Scanner(System.in);
        System.out.println("请输入水的重量");
        double m = in.nextDouble();
        System.out.println("请输入水的初始温度:");
        double tem1 = in.nextDouble();
        System.out.println("请输入水的初始温度:");
        double tem2 = in.nextDouble();
        System.out.println("需要的能量为:" + m * (tem2 - tem1) * 4184);
    }
    public static void main(String[] args){
        System.out.println("question1:");
        func1();
        System.out.println();

        System.out.println("question2:");
        func2();
        System.out.println();
    }
}
