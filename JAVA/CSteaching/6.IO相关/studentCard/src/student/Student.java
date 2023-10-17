package student;

public class Student{
    private String name;
    private String studentID;
    private CampusCard campusCard;
    private String enrollmentYear; //入学年份
    private String deptartment; //专业
    private String phoneNumber; //联系方式

    public Student(String studentID, String name, String enrollmentYear, String deptartment, String phoneNumber, String cardID){
        this.studentID = studentID;
        this.name = name;
        this.enrollmentYear = enrollmentYear;
        this.deptartment = deptartment;
        this.phoneNumber = phoneNumber;
        this.campusCard = new CampusCard(cardID);
    }

    public String getName() {
        return name;
    }

    public String getStudentID() {
        return studentID;
    }

    public String getEnrollmentYear(){return enrollmentYear;}

    public String getDeptartment(){return deptartment;}

    public String getPhoneNumber(){return phoneNumber;}

    public CampusCard getCampusCard() {
        return campusCard;
    }
}

