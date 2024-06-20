
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

//하노이탑 이동 순서
public class Main {
	static int count;
	static StringBuilder sb = new StringBuilder();
	
	private static void sol(int n, int start, int mid, int end) {
		if (n==0) return;
		sol(n-1,start,end,mid);
//		System.out.println(start+" "+end);
		sb.append(start+" "+end+"\n");
		count+=1;
		sol(n-1,mid,start,end);
		
	}

	public static void main(String[] args) throws Exception {

		//입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//출력
		int n = Integer.parseInt(br.readLine());
		sol(n,1,2,3);
		System.out.println(count);
		System.out.println(sb.toString());

	}


}
