package data;

public class stdcard {
    private String studentID;
    private String cardNumber;

    public stdcard(String studentID, String cardNumber){
        this.studentID = studentID;
        this.cardNumber = cardNumber;
    }
    public String getStudentID(){
        return studentID;
    }
    public String getCardNumber(){
        return cardNumber;
    }
}
