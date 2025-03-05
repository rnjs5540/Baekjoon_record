class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int[] dh = {0, -1, 0, 1};
        int[] dw = {1, 0, -1, 0};
        
        for (int i = 0; i < 4; i++) {
            int nh = h + dh[i];
            int nw = w + dw[i];
            if (nh >= 0 && nh < board.length &&
                nw >= 0 && nw < board.length &&
                board[h][w].equals(board[nh][nw])) {
                answer++;
            }
        }
        
        return answer;
    }
}