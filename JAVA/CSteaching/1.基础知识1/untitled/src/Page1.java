public class Page1 {

    public static void func1() {
        for (int row = 0; row < 4; row++) {
            for (int column = 0; column < 3; column++) {
                System.out.printf("%-5d", (int) Math.pow(row + 1, column + 1));
            }
            System.out.println();
        }
    }

    public static void func2() {
        final float radius = 5.5F;
        final float pi = 3.14F;
        System.out.println("圆的周长为: " + 2 * pi * radius);
        System.out.println("圆的面积为: " + pi * radius * radius);
    }

    public static void func3() {
        final float km_per_miles = 1.6F;
        System.out.println(14 * 3600 / ((45 * 60 + 30) * km_per_miles) + " miles/hour");
    }

    public static void main(String[] args) {
        System.out.println("question1:");
        func1();
        System.out.println();

        System.out.println("question2:");
        func2();
        System.out.println();

        System.out.println("question3:");
        func3();
        System.out.println();
    }
}
