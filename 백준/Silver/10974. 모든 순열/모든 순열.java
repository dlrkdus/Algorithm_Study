
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
	static int N;
	static int [] a;
	static int [] b;
	static boolean[] v;
	private static void perm(int cnt) {
		if(cnt==N) {
			for (int j = 0; j< b.length; j++) {
				System.out.print(b[j]+" ");
			}
			System.out.println();
			return;
		}
		for (int i=0; i<N; i++) {
			if (v[i]) continue;
			v[i]=true;
			b[cnt] = a[i];
			perm(cnt+1);
			v[i]=false;
		}
		
	}
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		
		a = IntStream.range(1, N + 1).toArray();
		b = new int [N];
		v = new boolean [N];
	
		perm(0);
		

	}



}
