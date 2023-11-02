import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Main {

    public static boolean canMove(int channel, Set<Integer> brokenButtons) {
        for (char ch : Integer.toString(channel).toCharArray()) {
            if (brokenButtons.contains(Character.getNumericValue(ch))) {
                return false;
            }
        }
        return true;
    }

    public static int minPresses(int targetChannel, Set<Integer> brokenButtons) {
        int minPress = Math.abs(targetChannel - 100);
        
        for (int i = 0; i < 1000001; i++) {
            int channel = targetChannel - i;
            if (channel >= 0 && canMove(channel, brokenButtons)) {
                minPress = Math.min(minPress, Integer.toString(channel).length() + i);
            }

            channel = targetChannel + i;
            if (canMove(channel, brokenButtons)) {
                minPress = Math.min(minPress, Integer.toString(channel).length() + i);
            }
        }
        return minPress;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int targetChannel = scanner.nextInt();
        int numBroken = scanner.nextInt();
        Set<Integer> brokenButtons = new HashSet<>();

        for (int i = 0; i < numBroken; i++) {
            brokenButtons.add(scanner.nextInt());
        }
        scanner.close();

        System.out.println(minPresses(targetChannel, brokenButtons));
    }
}
