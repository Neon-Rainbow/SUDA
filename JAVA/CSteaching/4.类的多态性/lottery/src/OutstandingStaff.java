public class OutstandingStaff extends staff {

    public OutstandingStaff() {
        super("Outstanding Staff");
    }

    public int recordLabel() { //200-3000以内没有数字附合该要求，最接近的两个数字为145和40585
        int[] nums = super.getArray(20);
        int label = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                label += num;
            } else {
                label -= num;
            }
        }
        return Math.abs(label);
    }
}
