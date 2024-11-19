import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static int[][] directions = new int[4][2];

    public static int[] turnLeft(int[] direction) {
        for (int i = 0; i < 4; i++) {
            if (Arrays.equals(direction, directions[i])) {
                return directions[(i+1) % 4];
            }
        }
        return null;
    }

    public static int[] turnRight(int[] direction) {
        for (int i = 0; i < 4; i++) {
            if (Arrays.equals(direction, directions[i])) {
                return directions[(i+4-1) % 4];
            }
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        directions[0] = new int[]{1, 0};
        directions[1] = new int[]{0, 1};
        directions[2] = new int[]{-1, 0};
        directions[3] = new int[]{0, -1};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int mapLength = Integer.parseInt(st.nextToken());
        int lineCount = Integer.parseInt(st.nextToken());
        int[] direction = {1, 0};
        int[] currentPosition = {0, 0};

        for (int lineIndex = 0; lineIndex < lineCount; lineIndex++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int option = Integer.parseInt(st.nextToken());
            switch(command) {
                case "TURN":
                    direction = option == 0 ? turnLeft(direction) : turnRight(direction);
                    break;
                case "MOVE":
                    currentPosition[0] += direction[0] * option;
                    currentPosition[1] += direction[1] * option;
                    if (currentPosition[0] < 0 || currentPosition[0] > mapLength
                        || currentPosition[1] < 0 || currentPosition[1] > mapLength) {
                        System.out.println(-1);
                        System.exit(0);
                    }
            }
        }
        System.out.println(currentPosition[0] + " " + currentPosition[1]);

    }
}
