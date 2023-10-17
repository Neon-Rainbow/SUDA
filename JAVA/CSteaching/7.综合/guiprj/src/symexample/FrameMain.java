package symexample;

import student.*;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

public class FrameMain {
    List<Student> allstudents = new ArrayList<>();
    HashMap<String,StudentValue> hashMap = new HashMap<>();
    //主界面
    JFrame frame = new JFrame("FrameMain");
    JMenuBar jMenuBar = new JMenuBar();
    JMenu menu = new JMenu("菜单");
    JMenuItem registerMenuItem = new JMenuItem("注册");
    JMenuItem searchMenuItem = new JMenuItem("查询");
    JMenuItem exitMenuItem = new JMenuItem("退出");
    //三个小界面
    JDialog frameRegister = new JDialog(frame, "FrameRegister", false);
    JDialog frameBrowse = new JDialog(frame, "FrameBrowse", false);
    JDialog frameClose = new JDialog(frame, "FrameClose", false);
    //frameRegister界面
    JLabel studentIDLabel_frameRegister = new JLabel("学生学号");
    JTextField studentIDTextField_frameRegister = new JTextField("");
    Box boxStudentID = Box.createHorizontalBox();
    JLabel studentNameLabel_frameRegister = new JLabel("学生姓名");
    JTextField studentNameTextField_frameRegister = new JTextField("");
    Box boxStudentName = Box.createHorizontalBox();
    JLabel sexLabel_frameRegister = new JLabel("性别:");
    JRadioButton male = new JRadioButton("男", true);
    JRadioButton female = new JRadioButton("女", false);
    ButtonGroup sexGroup = new ButtonGroup();
    Box boxSex = Box.createHorizontalBox();
    JLabel cityLabel = new JLabel("城市:");
    String[] cityList = {"苏州", "无锡", "常州", "镇江", "南京", "扬州", "泰州", "南通", "连云港", "盐城", "宿迁", "淮安", "徐州","其他"};
    Box boxCity = Box.createHorizontalBox();
    JComboBox<String> cityChooser = new JComboBox<>(cityList);
    JLabel favouritesLabel = new JLabel("爱好:");
    JTextField favouritesTextField = new JTextField("");
    Box boxFavourites = Box.createHorizontalBox();
    JButton addStudentButton = new JButton("新增学生信息");
    JButton saveStudentButton = new JButton("保存学生信息");
    Box boxButton = Box.createHorizontalBox();
    String savePilePath = "student.txt";
    JLabel saveStatus = new JLabel("状态");
    Box boxSaveStatus = Box.createHorizontalBox();
    Box boxFrameRegister = Box.createVerticalBox();

    //frameBrowse界面
    Box boxFrameBrowse = Box.createVerticalBox();
    JLabel countLabel_frameBrowse = new JLabel("目前展示的学生是第1位学生");
    JLabel studentIDLabel_frameBrowse = new JLabel("学生学号:");
    JLabel studentNameLabel_frameBrowse = new JLabel("学生姓名:");
    JLabel sexLabel_frameBrowse = new JLabel("学生性别:");
    JLabel studentCityLabel_frameBrowse = new JLabel("学生所在城市:");
    JLabel favouritesLabel_frameBrowse = new JLabel("学生爱好:");
    JLabel statusLabel = new JLabel("状态:");
    JButton nextButton = new JButton("next");
    JButton previousButton = new JButton("previous");
    Box boxButton_frameBrowse = Box.createHorizontalBox();
    int count = 0;
    String[] studentIDList;
    int studentIDListStartIndex;
    int studentIDListEndIndex;
    //frameClose界面
    JLabel closeLabel = new JLabel("是否真要退出？");
    JButton closeButton = new JButton("是");
    JButton notCloseButton = new JButton("否");
    JPanel closePanel = new JPanel();

    public void init() {
        //设置初始界面
        JPanel NorthPanel = new JPanel();
        jMenuBar.add(menu);
        menu.add(registerMenuItem);
        menu.add(searchMenuItem);
        menu.add(exitMenuItem);
        NorthPanel.add(jMenuBar);

        //设置注册界面
        frameRegister.setBounds(100, 100, 300, 200);
        frameRegister.setDefaultCloseOperation(JDialog.HIDE_ON_CLOSE);
        registerMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frameRegister.setVisible(true);
            }
        });
        sexGroup.add(male);
        sexGroup.add(female);

        boxStudentID.add(studentIDLabel_frameRegister);
        boxStudentID.add(studentIDTextField_frameRegister);
        boxStudentName.add(studentNameLabel_frameRegister);
        boxStudentName.add(studentNameTextField_frameRegister);
        boxSex.add(sexLabel_frameRegister);
        boxSex.add(male);
        boxSex.add(female);
        boxCity.add(cityLabel);
        boxCity.add(cityChooser);
        boxFavourites.add(favouritesLabel);
        boxFavourites.add(favouritesTextField);
        boxButton.add(addStudentButton);
        boxButton.add(saveStudentButton);
        boxSaveStatus.add(saveStatus);

        boxFrameRegister.add(boxStudentID);
        boxFrameRegister.add(boxStudentName);
        boxFrameRegister.add(boxSex);
        boxFrameRegister.add(boxCity);
        boxFrameRegister.add(boxFavourites);
        boxFrameRegister.add(boxButton);
        boxFrameRegister.add(boxSaveStatus);
        frameRegister.add(boxFrameRegister);

        addStudentButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Student student = new Student(studentIDTextField_frameRegister.getText(), studentNameTextField_frameRegister.getText(), sexChoice(male), cityChooser.getSelectedItem().toString().trim(), favouritesTextField.getText());
                saveStatus.setText("学号为" + studentIDTextField_frameRegister.getText() + "的学生的信息已经添加");
                allstudents.add(student);
            }
        });

        saveStudentButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                saveRegisterInformation(savePilePath);
                saveStatus.setText("学生信息已经保存至"+ savePilePath);
            }
        });

        //设置查询界面
        frameBrowse.setBounds(100, 100, 500, 200);
        frameBrowse.setDefaultCloseOperation(JDialog.HIDE_ON_CLOSE);
        searchMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frameBrowse.setVisible(true);
                readStudentInformation(savePilePath);
                Set<String> studentSet = hashMap.keySet();
                studentIDList = new String[studentSet.size()];
                studentSet.toArray(studentIDList);
                studentIDListStartIndex = 0;
                studentIDListEndIndex = studentIDList.length - 1;
                showStudentInformation(0);
            }
        });
        boxButton_frameBrowse.add(previousButton);
        boxButton_frameBrowse.add(nextButton);

        boxFrameBrowse.add(countLabel_frameBrowse);
        boxFrameBrowse.add(studentIDLabel_frameBrowse);
        boxFrameBrowse.add(studentNameLabel_frameBrowse);
        boxFrameBrowse.add(sexLabel_frameBrowse);
        boxFrameBrowse.add(studentCityLabel_frameBrowse);
        boxFrameBrowse.add(favouritesLabel_frameBrowse);
        boxFrameBrowse.add(boxButton_frameBrowse);
        boxFrameBrowse.add(statusLabel);
        frameBrowse.add(boxFrameBrowse);




        previousButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(count -1 < studentIDListStartIndex){
                    statusLabel.setText("状态:已经是第一个学生，无法读取前一个学生的信息");
                }else{
                    count = count - 1;
                    statusLabel.setText("状态:读取了前一个学生的信息");
                    countLabel_frameBrowse.setText("目前展示的学生是第" + (count+1) + "位学生");
                    //这里写一个函数用于展示学生信息
                    showStudentInformation(count);
                }
            }
        });

        nextButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(count + 1 > studentIDListEndIndex){
                    statusLabel.setText("状态:已经是最后一个学生，无法读取后一个学生的信息");
                }else{
                    count = count + 1;
                    statusLabel.setText("状态:读取了后一个学生的信息");
                    countLabel_frameBrowse.setText("目前展示的学生是第" + (count+1) + "位学生");
                    //这里写一个函数用于展示学生信息
                    showStudentInformation(count);
                }
            }
        });


        //设置关闭界面
        frameClose.setBounds(100, 100, 300, 200);
        frameClose.setDefaultCloseOperation(JDialog.HIDE_ON_CLOSE);
        exitMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frameClose.setVisible(true);
            }
        });
        closePanel.add(closeLabel, BorderLayout.NORTH);
        closePanel.add(closeButton, BorderLayout.SOUTH);
        closePanel.add(notCloseButton, BorderLayout.SOUTH);
        frameClose.add(closePanel);
        closeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        notCloseButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frameClose.setVisible(false);
            }
        });

        frame.add(NorthPanel, BorderLayout.NORTH);
        frame.setVisible(true);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    private String sexChoice(JRadioButton male) {
        if (male.isSelected()) {
            return "男";
        } else {
            return "女";
        }
    }

    private void saveRegisterInformation(String filepath) {
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter(filepath,true));
            for (Student student : allstudents) {
                bw.write(student.getStudentID() + " " + student.getStudentName() + " " + student.getSex() + " " + student.getCity() + " " + student.getFavourite());
                bw.newLine();
            }
            allstudents.clear();
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void readStudentInformation(String filepath){
        try{
            BufferedReader br = new BufferedReader(new FileReader(filepath));
            String line = null;
            while ((line = br.readLine())!= null){
                String[] data = line.split(" ");
                if(data.length == 5){
                    StudentValue studentValue = new StudentValue(data[1], data[2], data[3], data[4]);
                    String studentKey = data[0];
                    hashMap.put(studentKey, studentValue);
                }
            }
            br.close();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    private void showStudentInformation(int count){
        String studentID = studentIDList[count];
        String studentName = hashMap.get(studentID).getStudentName();
        String studentSex = hashMap.get(studentID).getSex();
        String studentCity = hashMap.get(studentID).getCity();
        String studentFavourite = hashMap.get(studentID).getFavourite();
        studentIDLabel_frameBrowse.setText("学生学号:" + studentID);
        studentNameLabel_frameBrowse.setText("学生姓名:" + studentName);
        studentCityLabel_frameBrowse.setText("学生所在城市:" + studentCity);
        sexLabel_frameBrowse.setText("学生性别:" + studentSex);
        favouritesLabel_frameBrowse.setText("学生爱好:" + studentFavourite);
    }
}

