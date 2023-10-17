public class SeniorManager extends staff {

    public SeniorManager() {
        super("Senior Manager");
    }

    public int recordLabel(){
        int[] nums = super.getArray(50);
        int maxSum = 0;
        int maxNum = 0;
        for (int j : nums) {
            int sum = 0;
            int num = j;
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            if (sum > maxSum) {
                maxSum = sum;
                maxNum = j;
            }
        }
        return maxNum;
    }
}
