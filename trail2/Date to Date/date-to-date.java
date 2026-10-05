import java.util.Scanner;
public class Main {

    static int[] month = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    static int monthSum(int m, int d) {
        int sum = 0;
        for(int i = 0; i < m; i++) {
            sum += month[i];
        }
        sum += d;
        return sum;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        System.out.print(monthSum(m2,d2) - monthSum(m1,d1) + 1);


        // Please write your code here.
    }
}