import java.util.Scanner;

public class Page6 {
    public static void func1(){
        Scanner in = new Scanner(System.in);
        System.out.println("请输入室外温度:");
        double t_a = in.nextDouble();
        System.out.println("请输入风速:");
        double v = in.nextDouble();
        double t_wc = 35.74 + 0.6215 * t_a - 35.75 * Math.pow(v,0.16) + 0.4275 * t_a * Math.pow(v, 0.16);
        System.out.println("室外温度为: " + t_wc);
    }

    public static void main(String[] args){
        System.out.println("question1:");
        func1();
        System.out.println();
    }
}
