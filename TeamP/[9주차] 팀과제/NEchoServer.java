//NEchoServer.java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

class ClientHandler extends Thread {
    private final Socket socket;
    private final int maxN = 1000;

    public ClientHandler(Socket socket) {
        this.socket = socket;
        setDaemon(true);
    }

    @Override
    public void run() {
        try (
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
            BufferedWriter writer = new BufferedWriter(
                new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8))
        ) {
            String line = reader.readLine();
            if (line == null) return;

            String[] parts = line.split("\\|", 2);
            if (parts.length != 2) {
                writeLine(writer, "ERR|BAD_REQUEST");
                return;
            }

            int n;
            try {
                n = Integer.parseInt(parts[0]);
            } catch (NumberFormatException e) {
                writeLine(writer, "ERR|BAD_REQUEST");
                return;
            }
            if (n < 1 || n > maxN) {
                writeLine(writer, "ERR|N_OUT_OF_RANGE");
                return;
            }

            String msg = parts[1];
            for (int i = 0; i < n; i++) {
                writeLine(writer, msg);
            }
        } catch (IOException ignored) {
        } finally {
            try { socket.close(); } catch (IOException ignored) {}
        }
    }

    private void writeLine(BufferedWriter writer, String s) throws IOException {
        writer.write(s);
        writer.write("\n");
        writer.flush();
    }
}

public class NEchoServer {
    private final int port;
    private final int backlog;

    public NEchoServer(int port, int backlog) {
        this.port = port;
        this.backlog = backlog;
    }

    public void start() throws IOException {
        try (ServerSocket server = new ServerSocket(this.port, this.backlog)) {
            System.out.println("[JAVA SERVER] Listening on 0.0.0.0:" + port);
            while (true) {
                Socket sock = server.accept();
                System.out.println("[JAVA SERVER] Connected: " + sock.getRemoteSocketAddress());
                new ClientHandler(sock).start();
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new NEchoServer(5050, 128).start();
    }
}
