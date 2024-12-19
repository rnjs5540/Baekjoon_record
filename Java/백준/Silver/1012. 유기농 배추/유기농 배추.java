import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int testCaseCount = Integer.parseInt(st.nextToken());
        for (int testCaseIndex = 0; testCaseIndex < testCaseCount; testCaseIndex++) {
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int[][] map = new int[M][N];

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                map[x][y] = 1;
            }

            // dfs
            int answer = 0;
            for (int x = 0; x < M; x++) {
                for (int y = 0; y < N; y++) {
                    if (map[x][y] == 1) {
                        answer += 1;
                        dfs(map, x, y, M, N);
                    }
                }
            }
            System.out.println(answer);
        }
    }

    public static void dfs(int[][] map, int x, int y, int M, int N) {
        if (map[x][y] != 1) {
            return;
        }
        map[x][y] = 2;

        if (y < N - 1) {
            dfs(map, x, y+1, M, N);
        }
        if (x > 0) {
            dfs(map, x-1, y, M, N);
        }
        if (y > 0) {
            dfs(map, x, y-1, M, N);
        }
        if (x < M - 1) {
            dfs(map, x+1, y, M, N);
        }
    }
}
