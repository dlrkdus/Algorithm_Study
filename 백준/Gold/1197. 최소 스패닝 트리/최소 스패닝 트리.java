import java.util.*;
import java.io.*;

class Main {
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken()); //정점
        int E = Integer.parseInt(st.nextToken()); //간선

        parent = new int[V]; //부모 노드 담을 배열 초기화 
        for (int i = 0; i < V; i++) {
            parent[i] = i;
        }

        List<Edge> edges = new ArrayList<>();

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken()) - 1;
            int v2 = Integer.parseInt(st.nextToken()) - 1;
            int dist = Integer.parseInt(st.nextToken());
            edges.add(new Edge(v1, v2, dist));
        }

        Collections.sort(edges); // 간선의 가중치를 오름차순 정렬해 작은 것부터 꺼낸다 

        int result = 0;
        for (Edge edge : edges) {
            if (find(edge.v1) != find(edge.v2)) { // # 부모가 같지 않다 = 같은 집합이 아니다 = 사이클이 아니다 
                union(edge.v1, edge.v2);
                result += edge.dist;
            }
        }

        System.out.println(result);
    }

    static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }

    static class Edge implements Comparable<Edge> {
        int v1, v2, dist;

        Edge(int v1, int v2, int dist) {
            this.v1 = v1;
            this.v2 = v2;
            this.dist = dist;
        }

        @Override
        public int compareTo(Edge other) {
            return this.dist - other.dist;
        }
    }
}