package student;

public class Student {
    private String studentID;
    private String studentName;
    private String sex;
    private String city;
    private String favourite;
    public Student(String studentID, String studentName, String sex, String city, String favourite){
        this.studentID = studentID;
        this.studentName = studentName;
        this.sex = sex;
        this.city = city;
        this.favourite = favourite;
    }
    public String getStudentID(){
        return studentID;
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
