import java.util.Scanner;

public class Main {
    static int[][] arr;
    static int bCount = 0;
    static int wCount = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        sol(0, 0, N);
        System.out.println(wCount);
        System.out.println(bCount);
    }

    static void sol(int x, int y, int N) {
        if (N == 1) {
            if (arr[x][y] == 0) {
                wCount++;
            } else {
                bCount++;
            }
            return;
        }

        int[][] a = new int[N][N];
        for (int i = 0; i < N; i++) {
            System.arraycopy(arr[x + i], y, a[i], 0, N);
        }

        boolean allWhite = true;
        boolean allBlack = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (a[i][j] != 0) {
                    allWhite = false;
                }
                if (a[i][j] != 1) {
                    allBlack = false;
                }
                if (!allWhite && !allBlack) {
                    break;
                }
            }
            if (!allWhite && !allBlack) {
                break;
            }
        }

        if (allWhite) {
            wCount++;
            return;
        }
        if (allBlack) {
            bCount++;
            return;
        }

        N /= 2;
        sol(x, y, N);
        sol(x, y + N, N);
        sol(x + N, y, N);
        sol(x + N, y + N, N);
    }
}
