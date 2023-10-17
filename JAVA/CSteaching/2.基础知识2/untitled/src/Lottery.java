import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class Lottery {
    public static void main(String[] args) {
        Set<Integer> lottery_pools = LotteryPools();
        System.out.println("下面是彩票游戏");
        System.out.println("请输入想要购买的彩票数量:");
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[] user = new int[count];
        int prime_cost = 2 * count;
        System.out.println("请输入要购买的彩票号码");
        for (int i = 0; i < count; i++) {
            if (scanner.hasNextInt()) {
                int number = scanner.nextInt();
                if (number >= 10 && number <= 999) {
                    user[i] = number;
                } else {
                    i--;
                    System.out.println("输入非法");
                }
            } else {
                System.out.println("输入非法");
                scanner.next();
                i--;
            }
        }
        int c = CorrectNumber(lottery_pools, user);
        int prize = GetPrize(c);
        int profit = prize - prime_cost;
        System.out.println("奖池中的数字为:");
        for (int number : lottery_pools) {
            System.out.print(number + " ");
        }
        System.out.println();
        System.out.println("成本为" + prime_cost + "元");
        System.out.println("奖金为" + prize + "元");
        if (profit > 0) {
            System.out.println("利润为" + profit + "元");
        } else if (profit < 0) {
            System.out.println("亏损为" + (-profit) + "元");
        } else {
            System.out.println("无亏损也无利润");
        }
    }

    public static Set<Integer> LotteryPools() {
        Set<Integer> lottery_numbers = new HashSet<>();
        Random random = new Random();
        while (lottery_numbers.size() < 10) {
            lottery_numbers.add(random.nextInt(999 - 10 + 1) + 10);
        }
        return lottery_numbers;
    }

    public static int CorrectNumber(Set<Integer> lottery_numbers, int[] user_numbers) {
        int count = 0;
        for (int number : user_numbers) {
            if (lottery_numbers.contains(number)) {
                count++;
            }
        }
        return count;
    }

    public static int GetPrize(int number) {
        if (number >= 7) {
            return 20000;
        } else if (number >= 5) {
            return 10000;
        } else if (number >= 3) {
            return 3000;
        } else if (number >= 1) {
            return 100;
        } else {
            return 0;
        }
    }
}
