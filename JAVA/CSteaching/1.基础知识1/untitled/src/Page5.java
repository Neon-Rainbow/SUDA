import java.util.Scanner;

public class Page5 {
    public static void func1(){
        final double pound_per_kilogram = 0.45359237;
        final double inch_per_meter = 0.0254;
        Scanner in = new Scanner(System.in);

        System.out.println("请输入体重，单位为磅:");
        double pound_weight = in.nextDouble();
        double kilogram_weight = pound_weight * pound_per_kilogram;

        System.out.println("请输入身高，单位为英尺:");
        double inch_height = in.nextDouble();
        double meter_height = inch_height * inch_per_meter;

        System.out.println("BMI:" + (kilogram_weight)/(meter_height * meter_height));
    }
    public static void func2(){
        Scanner in = new Scanner(System.in);
        System.out.println("请输入六边形的边长:");
        double length = in.nextDouble();
        System.out.println("六边形的面积为: " + 1.5 * Math.sqrt(3) * length * length);
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
