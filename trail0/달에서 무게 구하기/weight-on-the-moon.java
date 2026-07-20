public class Main {
    public static void main(String[] args) {
        int a = 13;
        double b = 0.165;
        double c = (a*100)*(b*100)/10000;
        System.out.printf("%d * %.6f = %.6f",a,b,c);
    }
}