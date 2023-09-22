import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    static class Edge {
        int start;
        int end;
        int weight;

        Edge(int start, int end, int weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }
    }

    static class UnionFind {
        private int[] parent;

        UnionFind(int V) {
            this.parent = new int[V + 1];
            Arrays.fill(this.parent, -1);
        }

        int find(int i) {
            if (parent[i] == -1)
                return i;
            return parent[i] = find(parent[i]);
        }

        boolean union(int a, int b) {
            int ancestorA = find(a);
            int ancestorB = find(b);
            if (ancestorA == ancestorB)
                return false;
            parent[ancestorB] = ancestorA;
            return true;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        Edge[] edges = new Edge[E];
        for (int i = 0; i < E; ++i) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            edges[i] = new Edge(start, end, weight);
        }

        Arrays.sort(edges, Comparator.comparingInt(e -> e.weight));

        int sum = 0;
        UnionFind uf = new UnionFind(V);

        for (Edge edge : edges) {
            if (uf.union(edge.start, edge.end)) {
                sum += edge.weight;
            }
        }

        System.out.println(sum);
    }
}
