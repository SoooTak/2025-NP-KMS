package Ch12;

// GUI_socket_JClient.java

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class GUI_socket_Jclient extends JFrame {

    private JTextField inputField;   // C 입력
    private JTextField outputField;  // F 출력
    private JButton sendButton;

    private Socket socket;
    private InputStream in;
    private OutputStream out;

    public GUI_socket_Jclient() {
        setTitle("Temperature Client");
        setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        initNetwork();
        initUI();
        initReceiverThread();

        pack();
        setLocationRelativeTo(null); // 화면 중앙
        setVisible(true);
    }

    // 파이썬: sock = socket(AF_INET, SOCK_STREAM); sock.connect(('127.0.0.1', 2500))
    private void initNetwork() {
        try {
            socket = new Socket("127.0.0.1", 2500);
            in = socket.getInputStream();
            out = socket.getOutputStream();
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "서버에 연결할 수 없습니다: " + e.getMessage(),
                    "연결 오류", JOptionPane.ERROR_MESSAGE);
            System.exit(1);
        }
    }

    // 파이썬 Tkinter 레이아웃을 Swing으로 그대로 옮김
    private void initUI() {
        JLabel messageLabel = new JLabel("Enter a temperature(C)");
        messageLabel.setFont(new Font("Verdana", Font.PLAIN, 16));

        JLabel recvLabel = new JLabel("Temperature in F");
        recvLabel.setFont(new Font("Verdana", Font.PLAIN, 16));

        inputField = new JTextField(5);
        inputField.setFont(new Font("Verdana", Font.PLAIN, 16));

        outputField = new JTextField(5);
        outputField.setFont(new Font("Verdana", Font.PLAIN, 16));
        outputField.setEditable(false);

        sendButton = new JButton("전송");
        sendButton.setFont(new Font("Verdana", Font.PLAIN, 12));
        sendButton.addActionListener(e -> calculate());

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5,5,5,5);
        gbc.anchor = GridBagConstraints.WEST;

        // row 0
        gbc.gridx = 0; gbc.gridy = 0;
        panel.add(messageLabel, gbc);

        gbc.gridx = 1;
        panel.add(inputField, gbc);

        gbc.gridx = 2;
        panel.add(sendButton, gbc);

        // row 1
        gbc.gridx = 0; gbc.gridy = 1;
        panel.add(recvLabel, gbc);

        gbc.gridx = 1;
        panel.add(outputField, gbc);

        add(panel);

        // 창 닫을 때 소켓 정리
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                cleanup();
                System.exit(0);
            }
        });
    }

    // 파이썬 calculate(): temp = float(entry1.get()); sock.send(str(temp).encode())
    private void calculate() {
        String text = inputField.getText().trim();
        if (text.isEmpty()) {
            return;
        }
        try {
            // 유효성 체크용
            Double.parseDouble(text);
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "숫자를 입력하세요.", "입력 오류",
                    JOptionPane.WARNING_MESSAGE);
            return;
        }

        try {
            byte[] data = text.getBytes(StandardCharsets.UTF_8);
            out.write(data);
            out.flush();
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(this, "서버 전송 중 오류: " + ex.getMessage(),
                    "전송 오류", JOptionPane.ERROR_MESSAGE);
        }
    }

    // 파이썬 handler()와 동일하게 백그라운드에서 recv(1024) 반복
    private void initReceiverThread() {
        Thread t = new Thread(() -> {
            byte[] buf = new byte[1024];
            try {
                while (true) {
                    int read = in.read(buf);
                    if (read == -1) {
                        break; // 연결 종료
                    }
                    String msg = new String(buf, 0, read, StandardCharsets.UTF_8);

                    SwingUtilities.invokeLater(() -> {
                        outputField.setText(msg);
                        inputField.setText("");
                    });
                }
            } catch (IOException e) {
                // 연결 종료 시 조용히 빠져나감
            } finally {
                cleanup();
            }
        });
        t.setDaemon(true); // 파이썬의 daemon = True
        t.start();
    }

    private void cleanup() {
        try {
            if (in != null) in.close();
        } catch (IOException ignored) {}
        try {
            if (out != null) out.close();
        } catch (IOException ignored) {}
        try {
            if (socket != null && !socket.isClosed()) socket.close();
        } catch (IOException ignored) {}
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(GUI_socket_Jclient::new);
    }
}
