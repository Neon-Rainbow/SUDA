import data.*;
import output.*;
import student.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Student> studentList = new ArrayList<>();
        List<stddata> stddataList = new ArrayList<>();
        List<recorddata> recorddataList = new ArrayList<>();
        List<stdcard> stdcardList = new ArrayList<>();
        String stddataFilePath = "studentCard/data/Stddata.txt";
        String stdcardFilePath = "studentCard/data/StdCard.txt";
        String recorddataFilePath = "studentCard/data/Recorddata.txt";

        try {
            BufferedReader stddataFile = new BufferedReader(new FileReader(stddataFilePath));
            String line1 = null;
            while((line1 = stddataFile.readLine())!= null){
                String[] data = line1.split(" ");
                if(data.length == 5){
                    stddataList.add(new stddata(data[0], data[1], data[2], data[3], data[4]));
                }
            }
            stddataFile.close();;
        }catch (IOException e){
            e.printStackTrace();
        }

        try {
            BufferedReader stdcardFile = new BufferedReader(new FileReader(stdcardFilePath));
            String line2 = null;
            while((line2 = stdcardFile.readLine())!= null){
                String[] data = line2.split(" ");
                if(data.length == 2){
                    stdcardList.add(new stdcard(data[0], data[1]));
                }
            }
            stdcardFile.close();
        }catch (IOException e){
            e.printStackTrace();
        }

        try {
            BufferedReader recorddataFile = new BufferedReader(new FileReader(recorddataFilePath));
            String line3 = null;
            while((line3 = recorddataFile.readLine()) != null){
                String[] data = line3.split(" ");
                if(data.length == 4){
                    recorddataList.add(new recorddata(data[0], data[1], new BigDecimal(data[2]), data[3]));
                }
            }
        }catch (IOException e){
            e.printStackTrace();
        }

        for(stddata sd:stddataList){
            for(stdcard sc:stdcardList){
                if(Objects.equals(sd.getStudentID(), sc.getStudentID())){
                    studentList.add(new Student(sd.getStudentID(), sd.getName(), sd.getEnrollmentYear(), sd.getDeptartment(), sd.getPhoneNumber(), sc.getCardNumber()));
                }
            }
        }

        for(recorddata rd:recorddataList){
            for(Student s:studentList){
                if(Objects.equals(rd.getCardNumber(), s.getCampusCard().getCardNumber())){
                    if(Objects.equals(rd.getType(), "0")){
                        s.getCampusCard().addBalance(rd.getAmount());
                        s.getCampusCard().addConsumption(new Consumption("0", rd.getAmount(), rd.getLocation()));
                    }else{
                        s.getCampusCard().consume(rd.getAmount());
                        s.getCampusCard().addConsumption(new Consumption("1", rd.getAmount(), rd.getLocation()));
                    }
                }
            }
        }

        List<outputStudentData> l = new ArrayList<>();
        for(Student s:studentList){
            outputStudentData output = new outputStudentData(s);
            l.add(output);
        }
        Collections.sort(l, Comparator.comparing(outputStudentData::getTotalConsumption));
        for(var v : l){
            System.out.println("********************");
            v.print1();
        }

        Collections.sort(l, (o1, o2) -> o2.getTotalSave().compareTo(o1.getTotalSave()));
        l.get(0).print2();
    }
}
