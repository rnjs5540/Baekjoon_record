import java.util.*;
import java.math.*;

class Solution {
    public int[] solution(int k, int[] score) {        
        List<Integer> answer = new ArrayList<>();
        
        List<Integer> jeondang = new ArrayList<>();
        int lowest = score[0];
        
        for (int i : score) {
            jeondang.add(i);
            jeondang.sort(Comparator.naturalOrder());
            jeondang = jeondang.subList(Math.max(jeondang.size() - k, 0), jeondang.size());
            
            answer.add(jeondang.get(0));
        }
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}