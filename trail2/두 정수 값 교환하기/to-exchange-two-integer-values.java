// 복습 : swap 과정에서 함수를 써야한다면 배열에 담는게 좋다.
//       CallByValue때문에 복사된 값을 쓰기에 return 해도 똑같다.
//       그리고 return값은 2개가 안된다.

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        // Please write your code here.
        int[] result = swap(n,m);
        n = result[0];
        m = result[1];
        System.out.print(n+" "+m);

    }
    static int[] swap(int a, int b){
        return new int[]{b, a};
    }
}