package data;

public class stddata {
        private String studentID;
        private String name;
        private String enrollmentYear;
        private String deptartment;
        private String phoneNumber;
        public stddata(String studentID, String name, String enrollmentYear, String deptartment, String phoneNumber){
            this.studentID = studentID;
            this.name = name;
            this.enrollmentYear = enrollmentYear;
            this.deptartment = deptartment;
            this.phoneNumber = phoneNumber;
        }

        public String getStudentID(){
            return studentID;
        }
        public String getName(){
            return name;
        }
        public String getEnrollmentYear(){
            return enrollmentYear;
        }
        public String getDeptartment(){
            return deptartment;
        }
        public String getPhoneNumber(){
        return phoneNumber;
    }
}
