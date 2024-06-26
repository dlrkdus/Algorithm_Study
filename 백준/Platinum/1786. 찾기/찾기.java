
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Arrays;

public class Main { // 문자열 일치 검사 알고리즘 

	public static void main(String[] args) throws IOException {
		String T; String P;

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = br.readLine();
		P = br.readLine();
		int [] F = new int [P.length()];

		
		for(int t=1, p=0; t<P.length(); t++) {
			while(p>0 && P.charAt(t)!=P.charAt(p)) p=F[p-1];
			if(P.charAt(t)==P.charAt(p)) F[t]=++p;
		}
//		System.out.println(Arrays.toString(F));	
		List<Integer> ans = new ArrayList<>();
		for(int t=0, p=0; t<T.length(); t++) {
			while(p>0 && T.charAt(t)!=P.charAt(p)) p=F[p-1];
			if(T.charAt(t)==P.charAt(p)) {
				if(p==P.length()-1) {
					ans.add(t-p);
					p=F[p];
				}else {
					++p;
				}
				
			}
		}
		System.out.println(ans.size());
		for (int num : ans) {
		    System.out.print(num+1 + " ");
		}
	}

}
