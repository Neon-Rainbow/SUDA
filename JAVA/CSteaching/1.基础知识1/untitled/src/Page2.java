import java.util.Scanner;

public class Page2 {
    public static long AuxiliaryFunction(int year, long population) {
        final long sec_per_year = 365 * 24 * 60 * 60;
        return population + year * (sec_per_year / 7 - sec_per_year / 15 + sec_per_year / 45);
    }

    public static void func1() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Year" + i + ": " + AuxiliaryFunction(i, 312032486));
        }

        Scanner in = new Scanner(System.in);
        System.out.print("year:");
        int year = in.nextInt();
        System.out.print("population:");
        long population = in.nextLong();
        System.out.println(AuxiliaryFunction(year, population));
    }

    public static void main(String[] args) {
        System.out.println("question1:");
        func1();
        System.out.println();
    }
}
