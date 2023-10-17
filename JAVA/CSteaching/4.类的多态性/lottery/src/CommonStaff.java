public class CommonStaff extends staff{
    public CommonStaff() {
        super("Common Staff");
    }

    public int recordLabel(){
        int label = 0;
        int[] nums = super.getArray(10);
        for(int i = 1; i < nums.length; i++){
            label += (nums[i] - nums[i - 1]);
        }
        return label;
    }
}
