// 복습: 문자열에서 배열처럼 꺼낼때는 .charAt()

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        String change = palin(input);
        System.out.print(input.equals(change)? "Yes":"No");
        // Please write your code here.
    }
    static String palin(String s) {
        String change = "";
        for(int i = s.length()-1; i >= 0 ; i--){
            change += s.charAt(i);
        }
        return change;
    }
}