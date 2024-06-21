
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
	static int N, M;
	static int [] a;
	static int [] b;	
    static StringBuilder sb = new StringBuilder();

	
	private static void comb(int cnt, int level) {

		if(cnt == M) {
			for(int i =0; i<M; i++) {
				sb.append(b[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		for(int i = level; i<N; i++) {
			b[cnt] = a[i];
			comb(cnt+1,i+1);
		}
	}
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		a = IntStream.range(1, N + 1).toArray();
		b = new int [M];
		
		comb(0,0);
		System.out.println(sb);
	
	}


}
