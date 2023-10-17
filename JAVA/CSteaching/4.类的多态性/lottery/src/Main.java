import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    List<staff> company;
    private Main(){
        this.company = initializeCompany();
    }

    private List<staff> initializeCompany() {
        List<staff> company = new ArrayList<staff>();
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入企业高管人数");
        int seniorNum = scanner.nextInt();
        System.out.println("请输入部门主管人数");
        int departNum = scanner.nextInt();
        System.out.println("请输入杰出员工人数");
        int outstandingNum = scanner.nextInt();
        System.out.println("请输入普通员工人数");
        int comNum = scanner.nextInt();
        for(int i = 0; i < seniorNum; i++){
            company.add(new SeniorManager());
        }
        for(int i = 0; i < departNum; i++){
            company.add(new DepartmentManager());
        }
        for(int i = 0; i < outstandingNum; i++){
            company.add(new OutstandingStaff());
        }
        for(int i = 0; i < comNum; i++){
            company.add(new CommonStaff());
        }
        return company;
    }

    static void play(staff stf){
        System.out.println("员工身份" + stf.getCategory());
        System.out.println("员工标签" + stf.recordLabel());
    }

    public static void main(String[] args) {
        Main  m = new Main();
        int count = 1;
        for(staff stf: m.company){
            System.out.println("第" + count + "位员工入场");
            System.out.println("员工身份为:" + stf.getCategory());
            System.out.println("员工标签为:" + stf.recordLabel());
            count++;
            System.out.println();
        }
    }
}