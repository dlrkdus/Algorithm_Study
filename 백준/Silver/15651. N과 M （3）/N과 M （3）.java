
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
	static int N,M;
	static int [] a;
	static int [] b;
	static StringBuilder sb = new StringBuilder();
	
	private static void perm(int cnt) {
		if(cnt==M) {
			for (int j = 0; j< b.length; j++) {
				sb.append(b[j]).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i=0; i<N; i++) {
			b[cnt] = a[i];
			perm(cnt+1);
		}
		
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		a = IntStream.range(1, N + 1).toArray();
		b = new int [M];
	
		perm(0);
		
		System.out.println(sb.toString());
		

	}



}
