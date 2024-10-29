import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n <= 2) { 
                System.out.println(1);
            } else {
                long[] arr = new long[n];
                arr[0] = 1;
                arr[1] = 1;
                arr[2] = 1;
                
                for (int j = 3; j < n; j++) {
                    arr[j] = arr[j - 2] + arr[j - 3];
                }
                
                System.out.println(arr[n - 1]);
            }
        }
    
    }
}