package frame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FanFrame {
    private JFrame f = new JFrame("Fan  control");
    private JButton openFanButton = new JButton("打开风扇"); //打开风扇的按钮
    private JButton closeFanButton = new JButton("关闭风扇"); //关闭风扇的按钮
    private JButton rotateFanButton = new JButton("风扇转头"); //风扇转头的按钮
    private JButton timesStart = new JButton("定时启动"); //定时启动按钮
    private JButton timedClose = new JButton("定时关闭"); //定时关闭按钮
    private JButton confirmButton = new JButton("输入完毕");
    private TextField timeTextField = new TextField(""); //输入时间
    private int latencyTime; //剩余时间
    private JLabel label1 = new JLabel("Fan Condition:close");
    private JLabel label2 = new JLabel("Latency Time:0sec");
    private boolean isFanOn = false;
    boolean timingEnded = false;
    String waitToDo;
    boolean s = false;
    private double angle = 0;
    myCanvas drawArea = new myCanvas();
    public void init(){
        Timer time = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(latencyTime > 0){
                    latencyTime = latencyTime - 1;
                    if(waitToDo.equals("open") && !isFanOn){
                        closeFanButton.doClick();
                    }else if(waitToDo.equals("close") && isFanOn){
                        openFanButton.doClick();
                    }
                }else if(!timingEnded){
                    if(waitToDo.equals("open")){
                        openFanButton.doClick();
                    }else if(waitToDo.equals("close")){
                        closeFanButton.doClick();
                    }
                    timingEnded = true;
                }
                label2.setText("Latency Time:" + latencyTime + "sec");
            }
        });

        openFanButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                label1.setText("fan condition:open");
                isFanOn = true;
                if(timingEnded){
                    time.stop();
                }
            }
        });
        closeFanButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                label1.setText("fan condition:close");
                isFanOn = false;
                if(timingEnded){
                    time.stop();
                }
            }
        });
        rotateFanButton.addActionListener(new rotateFanButtonListener());
        JPanel top = new JPanel();
        top.add(openFanButton);
        top.add(closeFanButton);
        top.add(rotateFanButton);
        top.add(label1);
        f.add(top, BorderLayout.NORTH);


        JPanel center = new JPanel();



        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                latencyTime = Integer.parseInt(timeTextField.getText());
                label2.setText("Latency Time:" + latencyTime + "sec");
            }
        });


        timesStart.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                waitToDo = "open";
                time.restart();
            }
        });
        timedClose.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                waitToDo = "close";
                time.restart();
            }
        });

        center.add(timesStart);
        center.add(timedClose);
        center.add(confirmButton);
        center.add(timeTextField);
        center.add(label2);
        f.add(center, BorderLayout.CENTER);

        Timer animationTimer = new Timer(100, new animationListener());
        animationTimer.start();

        drawArea.setPreferredSize(new Dimension(300, 200));
        f.add(drawArea, BorderLayout.SOUTH);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setBounds(100, 100, 600, 400);
        f.setVisible(true);
    }

    private class openFanButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            label1.setText("fan condition:open");
            isFanOn = true;
        }
    }
    private class closeFanButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            label1.setText("fan condition:close");
            isFanOn = false;
        }
    }
    private class animationListener implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e) {
            if(isFanOn){
                angle += 10;
                drawArea.repaint();
            }
        }
    }
    private class rotateFanButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if(isFanOn){
                label1.setText("fan condition:rotate");
            }
        }
    }
    private class myCanvas extends Canvas {
        @Override
        public void paint(Graphics g){
            Graphics2D g2d = (Graphics2D) g;
            //AffineTransform oldTransform = g2d.getTransform();
            g2d.rotate(Math.toRadians(angle), (double) getWidth() / 2, (double) getHeight() / 2);
            g2d.drawRect(getWidth() / 2 - 50, getHeight() / 2 - 50, 100, 100);
            //g2d.setTransform(oldTransform);
        }
    }
}

