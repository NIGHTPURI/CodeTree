import java.util.Scanner;
public class Main {
    static String season(int m) {
        if (m >= 3 && m <= 5) {
            return "Spring";
        } else if (m >= 6 && m <= 8) {
            return "Summer";
        } else if (m >= 9 && m <= 11) {
            return "Fall";
        } else {
            return "Winter";
        }
    }
    
    static boolean isReal(int y, int m, int d) {
        int[] day = {31,28,31,30,31,30,31,31,30,31,30,31};
        if(y%400 == 0 || (y%4 == 0 && y%100 !=0)) {
            day[1] = 29;
        }
        if(m < 1 || m > 12) {
            return false;
        }

        return d >= 1 && d <= day[m-1];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int y = sc.nextInt();
        int m = sc.nextInt();
        int d = sc.nextInt();
        // Please write your code here.
        System.out.println(isReal(y,m,d) ? season(m) : -1);

    }
}