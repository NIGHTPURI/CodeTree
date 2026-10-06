import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int[] ans = change(a, b);
        a = ans[0];
        b = ans[1];
        System.out.print(a + " " + b);
    }
    static int[] change(int a, int b) {
        if (a > b) {
            a += 25;
            b *= 2;
        } else {
            b += 25;
            a *= 2;
        }
        return new int[] {a, b};
    }
}
