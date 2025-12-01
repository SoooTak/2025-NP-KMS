package Ch11;

// CapsuleClient.java
import java.io.*;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.nio.charset.StandardCharsets;

public class CapsuleClient {

    private static final int SIZE = 5;
    private static final int HEADER_SIZE = 11; // START(1) + header(10)

    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 2500;

        try (Socket sock = new Socket(host, port)) {
            sock.setSoTimeout(100); // 파이썬 settimeout과 비슷하게 짧은 타임아웃
            InputStream in = sock.getInputStream();
            OutputStream out = sock.getOutputStream();

            int startByte = 0x05;
            int addr = 1;
            int no = 1;

            String msg = "hello world";
            System.out.println("전송 메시지: " + msg);

            // 1. 프레임 묶어서 전송
            StringBuilder frameSeq = new StringBuilder();

            for (int i = 0; i < msg.length(); i += SIZE) {
                int end = Math.min(i + SIZE, msg.length());
                String slice = msg.substring(i, end);
                frameSeq.append(frame(startByte, addr, no, slice));
                no++;
            }

            byte[] sendBytes = frameSeq.toString().getBytes(StandardCharsets.UTF_8);
            out.write(sendBytes);
            out.flush();

            // 2. 응답 수신 및 재조립
            StringBuilder rMsg = new StringBuilder();
            int seqNum = 1;
            byte[] oneByte = new byte[1];

            while (true) {
                try {
                    int read = in.read(oneByte);
                    if (read == -1) break; // 서버가 연결 종료

                    // START 바이트 확인
                    if ((oneByte[0] & 0xFF) == startByte) {
                        // 나머지 헤더 10바이트 읽기
                        byte[] headerBytes = readFully(in, HEADER_SIZE - 1);
                        String pMsg = new String(headerBytes, StandardCharsets.UTF_8);

                        // p_msg[2:6] → 시퀀스 번호
                        int recvSeq = Integer.parseInt(pMsg.substring(2, 6));
                        // 마지막 4자리 → payload 길이
                        int payloadLen = Integer.parseInt(pMsg.substring(pMsg.length() - 4));

                        if (recvSeq == seqNum) {
                            byte[] payloadBytes = readFully(in, payloadLen);
                            rMsg.append(new String(payloadBytes, StandardCharsets.UTF_8));
                            seqNum++;
                        } else {
                            // 시퀀스 안 맞으면 해당 payload는 버리기
                            skipFully(in, payloadLen);
                        }
                    }
                } catch (SocketTimeoutException e) {
                    // 더 이상 들어오는 데이터가 없으면 종료
                    break;
                }
            }

            System.out.println("복원 메시지: " + rMsg.toString());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * 파이썬 capsule.frame(START, ADDR, NO, payload)과 동일한 형식:
     * chr(START) + "%02d%04d%04d"%(ADDR, NO, len(payload)) + payload
     */
    private static String frame(int start, int addr, int no, String payload) {
        String header = String.format("%02d%04d%04d", addr, no, payload.length());
        return String.valueOf((char) start) + header + payload;
    }

    private static byte[] readFully(InputStream in, int len) throws IOException {
        byte[] buf = new byte[len];
        int off = 0;
        while (off < len) {
            int r = in.read(buf, off, len - off);
            if (r == -1) {
                throw new EOFException("예상보다 먼저 스트림이 종료되었습니다.");
            }
            off += r;
        }
        return buf;
    }

    private static void skipFully(InputStream in, int len) throws IOException {
        long remaining = len;
        while (remaining > 0) {
            long skipped = in.skip(remaining);
            if (skipped <= 0) {
                // skip이 안 되면 한 바이트씩 읽어서 버린다
                if (in.read() == -1) {
                    throw new EOFException("skip 중 스트림 종료");
                }
                skipped = 1;
            }
            remaining -= skipped;
        }
    }
}
