import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = 0;
        int maxLen = 0;
        Arrays.sort(mats);
        int maxMatSize = mats[mats.length - 1];
        
        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[0].length; j++) {
                int len = checkPark(park, i, j, maxMatSize);
                maxLen = Math.max(maxLen, len);
            }
        }
        
        answer = getAvailableMatSize(maxLen, mats);
        
        return answer;
    }
    
    private int checkPark(String[][] park, int i, int j, int maxMatSize) {  
        if (!park[i][j].equals("-1")) {
            return 0;
        }
        
        int len = 1;
        while (i + len < park.length && j + len < park[0].length) {
            // 오른쪽 줄, 아래쪽 줄 체크
            for (int tmp = 0; tmp <= len; tmp++) {
                if (!park[i+tmp][j+len].equals("-1") ||
                   !park[i+len][j+tmp].equals("-1")) {
                    return len;
                }
            }
            
            len++;
            if (len == maxMatSize) {
                break;
            }
        }
        
        return len;
    }
    
    
    private int getAvailableMatSize(int maxLen, int[] mats) {
        int choosedSize = -1;
        for (int mat : mats) {
            if (mat <= maxLen) {
                choosedSize = mat;
            }
            else {
                break;
            }
        }
        
        return choosedSize;
    }
}