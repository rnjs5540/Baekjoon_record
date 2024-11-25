import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int strLen = (int) Math.pow(3, n);
            System.out.println(cantor(n, "-".repeat(strLen)));
        }
    }

    public static String cantor(int n, String str) {
        if (n == 0)
            return str;

        int strLen = (int) Math.pow(3, n);
        String str1 = str.substring(0, strLen/3);
        String str2 = " ".repeat(strLen/3);
        String str3 = str.substring(strLen/3 * 2);
        return cantor(n-1, str1) + cantor(n-1, str2) + cantor(n-1, str3);
    }
}