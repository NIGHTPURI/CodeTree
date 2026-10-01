import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
            modify(arr, i);
            System.out.print(arr[i]+" ");
        }
    }
    static void modify(int[] arr, int x) {
        if(arr[x] % 2 == 0) {
            arr[x] /= 2;
        }
    }
}