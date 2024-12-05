import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        List<Integer> answerList = new ArrayList<>();
        int last = -1;
        
        for (int i : arr) {
            if (last != i) {
                answerList.add(i);
                last = i;
            }
        }
        
        return answerList.stream().mapToInt(Integer::intValue).toArray();
    }
}