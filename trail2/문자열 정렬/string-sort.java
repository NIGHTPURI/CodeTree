import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        char[] str = s.toCharArray();
        Arrays.sort(str);
        for(int i=0; i < s.length(); i++) {
            System.out.print(str[i]);
        }
        // Please write your code here.
    }
}