package student;

public class StudentValue {
    private String studentName;
    private String sex;
    private String city;
    private String favourite;
    public StudentValue(String studentName, String sex, String city, String favourite){
        this.studentName = studentName;
        this.sex = sex;
        this.city = city;
        this.favourite = favourite;
    }
    public String getStudentName(){
        return studentName;
    }
    public String getSex(){
        return sex;
    }
    public String getCity(){
        return city;
    }
    public String getFavourite(){
        return favourite;
    }
}
