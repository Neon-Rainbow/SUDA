public abstract class staff {
    private final String category; //员工的类别

    public staff(String category) { //构造函数
        this.category = category;
    }

    public String getCategory(){
        return this.category;
    }
    public abstract int recordLabel();

    public int[] getArray(int size){ //生成长度为size的随机数的数组。其中size是由员工的类别决定
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = (int)(Math.random() * (3000 - 200 + 1)) + 200;
        }
        return array;
    }
}
