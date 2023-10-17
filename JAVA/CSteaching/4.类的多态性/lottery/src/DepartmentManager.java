public class DepartmentManager extends staff{
    public DepartmentManager() {
        super("Department Manager");
    }

    public int recordLabel(){
        int label = 0;
        int[] nums = super.getArray(30);
        for(int num:nums){
            if(num % 2 == 0){
                label += num;
            }else{
                label -= num;
            }
        }
        return Math.abs(label);
    }
}
