import java.util.*;
import java.io.*;

public class Main {
    public static void main (String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] visited = new int[100001];
        visited[N] = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(N);

        while (!queue.isEmpty()) {
            int current = queue.remove();
            if (current == K) {
                System.out.println(visited[current]);
                break;
            }

            if (current > 0 && visited[current-1] == 0) {
                visited[current-1] = visited[current] + 1;
                queue.add(current-1);
            }
            if (current < 100000 && visited[current+1] == 0) {
                visited[current+1] = visited[current] + 1;
                queue.add(current+1);
            }
            if (current <= 50000 && visited[current*2] == 0) {
                visited[current*2] = visited[current] + 1;
                queue.add(current*2);
            }
        }
    }
}
