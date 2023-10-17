public class Student{
    private String name;
    private String studentID;
    private CampusCard campusCard;

    public Student(String name,String studentID){
        this.name = name;
        this.studentID = studentID;
        this.campusCard = new CampusCard(studentID);
    }

    public String getName() {
        return name;
    }

    public String getStudentID() {
        return studentID;
    }

    public CampusCard getCampusCard() {
        return campusCard;
    }
}

