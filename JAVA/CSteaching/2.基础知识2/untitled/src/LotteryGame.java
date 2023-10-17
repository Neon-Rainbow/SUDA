import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class LotteryGame {
    private static final int MIN_NUMBER = 10;
    private static final int MAX_NUMBER = 999;
    private static final int FIRST_PRIZE = 20000;
    private static final int SECOND_PRIZE = 10000;
    private static final int THIRD_PRIZE = 3000;
    private static final int ENCOURAGEMENT_PRIZE = 100;

    public static void main(String[] args) {
        Set<Integer> lotteryNumbers = generateLotteryNumbers();
        System.out.println("欢迎来到彩票游戏！");
        System.out.println("彩票池中的数字为：" + lotteryNumbers);
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入您想购买的数字数量：");
        int count = scanner.nextInt();
        int[] userNumbers = new int[count];
        int totalPrice = count * 2;
        System.out.println("您需要支付" + totalPrice + "元。");
        System.out.println("您可以自己输入数字，也可以由机器自动生成。");
        System.out.println("请依次输入" + count + "个数字：");
        for (int i = 0; i < count; i++) {
            if (scanner.hasNextInt()) {
                int number = scanner.nextInt();
                if (number < MIN_NUMBER || number > MAX_NUMBER) {
                    System.out.println("输入的数字不合法，请重新输入。");
                    i--;
                } else {
                    userNumbers[i] = number;
                }
            } else {
                System.out.println("输入的数字不合法，请重新输入。");
                scanner.next();
                i--;
            }
        }
        System.out.println("您选择的数字为：" + arrayToString(userNumbers));
        int[] distinctNumbers = getDistinctNumbers(userNumbers);
        int matchedCount = countMatchedNumbers(lotteryNumbers, distinctNumbers);
        int prize = calculatePrize(matchedCount);
        int profit = prize - totalPrice;
        System.out.println("恭喜您中了" + prize + "元！");
        if (profit > 0) {
            System.out.println("您的利润为" + profit + "元。");
        } else if (profit < 0) {
            System.out.println("很遗憾，您亏损了" + (-profit) + "元。");
        } else {
            System.out.println("您没有盈利也没有亏损。");
        }
    }

    private static Set<Integer> generateLotteryNumbers() {
        Set<Integer> lotteryNumbers = new HashSet<>();
        Random random = new Random();
        while (lotteryNumbers.size() < 10) {
            lotteryNumbers.add(random.nextInt(MAX_NUMBER - MIN_NUMBER + 1) + MIN_NUMBER);
        }
        return lotteryNumbers;
    }

    private static String arrayToString(int[] array) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < array.length; i++) {
            sb.append(array[i]);
            if (i < array.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

    private static int[] getDistinctNumbers(int[] numbers) {
        Set<Integer> distinctNumbers = new HashSet<>();
        for (int number : numbers) {
            distinctNumbers.add(number);
        }
        int[] result = new int[distinctNumbers.size()];
        int index = 0;
        for (int number : distinctNumbers) {
            result[index++] = number;
        }
        return result;
    }

    private static int countMatchedNumbers(Set<Integer> lotteryNumbers, int[] userNumbers) {
        int count = 0;
        for (int number : userNumbers) {
            if (lotteryNumbers.contains(number)) {
                count++;
            }
        }
        return count;
    }

    private static int calculatePrize(int matchedCount) {
        if (matchedCount >= 7) {
            return FIRST_PRIZE;
        } else if (matchedCount >= 5) {
            return SECOND_PRIZE;
        } else if (matchedCount >= 3) {
            return THIRD_PRIZE;
        } else if (matchedCount >= 1) {
            return ENCOURAGEMENT_PRIZE;
        } else {
            return 0;
        }
    }
}