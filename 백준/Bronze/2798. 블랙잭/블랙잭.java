
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int [] a;
    static int max = -1000;
	
	private static void sol(int cnt, int level, int sum) {
		if (sum>M) return;
		if (cnt ==3) {
			max = Math.max(max, sum);
		}
		else{
			for(int i=level; i<N; i++) {
			sol(cnt+1,i+1,sum+a[i]);
			}
		}
		
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		a = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
		
		sol(0,0,0);
		System.out.println(max);

	}





}
