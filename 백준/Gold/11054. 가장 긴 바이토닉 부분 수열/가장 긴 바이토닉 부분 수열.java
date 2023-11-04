import java.util.Scanner;

public class Main {
    static final int UP = 0;
    static final int DOWN = 1;
    static int[] nums;
    static int[][] maxLengths;


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        nums = new int[n];
        for (int i = 0; i < n; ++i)
            nums[i] = sc.nextInt();


        maxLengths = new int[n][2];
        for (int pre = 0; pre < n; ++pre) {
            for (int cur = pre + 1; cur < n; ++cur) {
                goWithStart(pre, cur);  // pre에서 부분수열 시작할 경우
                goWithUp(pre, cur);     // pre에서 증가하던 수열을 받아서 갈 경우
                goWithDown(pre, cur);   // pre에서 감소하던 수열을 받아서 갈 경우
            }
        }

        int maxLength = 1;
        for (int i = 0; i < n; ++i) {
            maxLength = Math.max(maxLength, maxLengths[i][UP]);
            maxLength = Math.max(maxLength, maxLengths[i][DOWN]);
        }

        System.out.println(maxLength);
    }

    static void goWithStart(int pre, int cur) {
        // 증가
        if (nums[pre] < nums[cur])
            maxLengths[cur][UP] = Math.max(maxLengths[cur][UP], 2);
        // 감소
        else if (nums[pre] > nums[cur])
            maxLengths[cur][DOWN] = Math.max(maxLengths[cur][DOWN], 2);
    }
    static void goWithUp(int pre, int cur) {
        if (maxLengths[pre][UP] == 0)
            return;
        // 증증
        if (nums[pre] < nums[cur])
            maxLengths[cur][UP] = Math.max(maxLengths[cur][UP], maxLengths[pre][UP] + 1);
        // 증감
        else if (nums[pre] > nums[cur])
            maxLengths[cur][DOWN] = Math.max(maxLengths[cur][DOWN], maxLengths[pre][UP] + 1);
    }
    static void goWithDown(int pre, int cur) {
        if (maxLengths[pre][DOWN] == 0)
            return;
        // 감증
        if (nums[pre] < nums[cur])
            maxLengths[cur][UP] = Math.max(maxLengths[cur][UP], 2);
        // 감감
        else if (nums[pre] > nums[cur])
            maxLengths[cur][DOWN] = Math.max(maxLengths[cur][DOWN], maxLengths[pre][DOWN] + 1);
    }
}