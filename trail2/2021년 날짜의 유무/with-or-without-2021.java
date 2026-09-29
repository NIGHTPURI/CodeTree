import java.util.Scanner;
public class Main {
    static boolean isReal(int m, int d) {
        int[] day = {0,31,28,31,30,31,30,31,31,30,31,30,31};

        if ((m < 1) || (m > 12)) {
            return false;
        }

        return (d > 0) && (d <= day[m]);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int d = sc.nextInt();

        System.out.println(isReal(m,d) ? "Yes" : "No");



        // Please write your code here.
    }
}