import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
     private static List<Student> students = new ArrayList<>();

     public static void main(String[] args){
          Scanner scanner = new Scanner(System.in);
          while(true){
               System.out.println("请选择操作：");
               System.out.println("1. 添加学生信息");
               System.out.println("2. 添加消费记录");
               System.out.println("3. 输出消费记录");
               System.out.println("4. 退出");
               int choice = scanner.nextInt();
               switch (choice){
                    case 1:
                         addStudent(scanner);
                         break;
                    case 2:
                         addConsumption(scanner);
                         break;
                    case 3:
                         printConsumption(scanner);
                         break;
                    case 4:
                         return;
                    default:
                         System.out.println("选择错误");
               }
          }
     }



     private static void addStudent(Scanner scanner) {
          System.out.println("请输入学生姓名：");
          String name = scanner.next();
          System.out.println("请输入学生学号：");
          String studentID = scanner.next();
          students.add(new Student(name, studentID));
          System.out.println("学生信息添加成功。");
     }

     private static void addConsumption(Scanner scanner){
          System.out.println("请输入学生的学号");
          String studentID = scanner.next();
          Student student = findStudentName(studentID);
          if(student == null){
               System.out.println("未找到该学生，请检查学号是否正确");
               return;
          }
          System.out.println("请输入消费的时间");
          String time = scanner.next();
          System.out.println("请输入消费的金额");
          double amount = scanner.nextDouble(); //amount 消费金额
          System.out.println("请输入消费地点：");
          String location = scanner.next();
          student.getCampusCard().Consume(amount);
          Consumption consumption  = new Consumption(time, amount, location);
          student.getCampusCard().addConsumption(consumption);
     }
     private static void printConsumption(Scanner scanner) {
          System.out.println("请输入学生的学号");
          String studentID = scanner.next();
          Student student = findStudentName(studentID);
          if(student == null){
               System.out.println("未找到该学生，请检查学号是否正确");
               return;
          }
          for(Consumption consumption:student.getCampusCard().getConsumption()){
               System.out.println("消费时间:" + consumption.getTime());
               System.out.println("消费地点:" + consumption.getLocation());
               System.out.println("消费金额:" + consumption.getAmount());
               System.out.println();
          }
     }

     private static Student findStudentName(String studentID){
          for(Student student:students){
               if(student.getStudentID().equals(studentID)){
                    return student;
               }
          }
          return null;
     }
}
