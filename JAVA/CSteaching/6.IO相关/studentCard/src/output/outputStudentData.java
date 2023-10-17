package output;

import java.io.*;
import java.math.BigDecimal;
import java.util.Objects;

import student.*;

public class outputStudentData {
    private Student student;

    public outputStudentData(Student student) {
        this.student = student;
    }

    public void print1() {
        System.out.println("学号:" + student.getStudentID());
        System.out.println("姓名:" + student.getName());
        System.out.println("入学年份:" + student.getEnrollmentYear());
        System.out.println("专业:" + student.getDeptartment());
        System.out.println("联系方式:" + student.getPhoneNumber());
        System.out.println("卡号:" + student.getCampusCard().getCardNumber());
        System.out.println("余额:" + student.getCampusCard().getBalance());
        System.out.println("该卡总消费:" + student.getCampusCard().getTotalConsumption());
    }

    public void print2(){
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter("SaveTop.txt"));
            bw.write("***************************");
            bw.newLine();
            bw.write("学号:" + student.getStudentID());
            bw.newLine();
            bw.write("姓名:" + student.getName());
            bw.newLine();
            bw.write("入学年份:" + student.getEnrollmentYear());
            bw.newLine();;
            bw.write("专业:" + student.getDeptartment());
            bw.newLine();
            bw.write("联系方式:" + student.getPhoneNumber());
            bw.newLine();
            bw.write("卡号:" + student.getCampusCard().getCardNumber());
            bw.newLine();
            bw.write("余额:" + student.getCampusCard().getBalance());
            bw.newLine();
            bw.write("该卡的详细消费情况:");
            bw.newLine();
            for(var consumption:student.getCampusCard().getConsumption()){
                if(Objects.equals(consumption.getType(), "0")){
                    bw.write("存钱 金额" + consumption.getAmount() + "消费地点" + consumption.getLocation());
                    bw.newLine();
                }else{
                    bw.write("消费 金额" + consumption.getAmount() + "消费地点" + consumption.getLocation());
                    bw.newLine();
                }
            }
            bw.write("该卡总消费:" + student.getCampusCard().getTotalConsumption());
            bw.newLine();
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public BigDecimal getBalance() {
        return student.getCampusCard().getBalance();
    }

    public BigDecimal getTotalConsumption() {
        return student.getCampusCard().getTotalConsumption();
    }

    public BigDecimal getTotalSave() {
        return student.getCampusCard().getTotalSave();
    }

    public Student getStudent(){
        return student;
    }
}
