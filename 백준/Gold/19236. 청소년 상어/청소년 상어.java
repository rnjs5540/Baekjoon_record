import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] dirR = {999, -1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dirC = {999, 0, -1, -1, -1, 0, 1, 1, 1};
    static class Fish {
        int r;
        int c;
        int num;
        int dir;
        Fish(int r, int c, int num, int dir) {
            this.r = r;
            this.c = c;
            this.num = num;
            this.dir = dir;
        }
        Fish(){}
        public static Fish copy(Fish original){
            Fish copyObject = new Fish();
            copyObject.r = original.r;
            copyObject.c = original.c;
            copyObject.num = original.num;
            copyObject.dir = original.dir;
            return copyObject;
        }
        void move(Fish[][] fishMap) {
            int nr = r + dirR[dir];
            int nc = c + dirC[dir];
            int initialDir = dir;
            while (nr < 0 || nr >= 4 || nc < 0 || nc >= 4
                || fishMap[nr][nc].num == 's') {
                dir = (dir + 1) % 9;
                if (dir == initialDir)
                    return;
                nr = r + dirR[dir];
                nc = c + dirC[dir];
            }

            Fish tmp = fishMap[nr][nc];
            fishMap[nr][nc] = fishMap[r][c];
            fishMap[r][c] = tmp;
            fishMap[r][c].r = r;
            fishMap[r][c].c = c;
            fishMap[nr][nc].r = nr;
            fishMap[nr][nc].c = nc;
        }
    }
    static class TeenShark {
        int r;
        int c;
        int dir;
        int eatenFishSum = 0;
        TeenShark(int r, int c, int dir, int eatenFishSum) {
            this.r = r;
            this.c = c;
            this.dir = dir;
            this.eatenFishSum = eatenFishSum;
        }
        TeenShark(){};
        public static TeenShark copy(TeenShark original){
            TeenShark copyObject = new TeenShark();
            copyObject.r = original.r;
            copyObject.c = original.c;
            copyObject.dir = original.dir;
            copyObject.eatenFishSum = original.eatenFishSum;
            return copyObject;
        }
        void move(Fish[][] fishMap, int nr, int nc) {
            this.eatenFishSum += fishMap[nr][nc].num;
            fishMap[this.r][this.c].num = 0;
            this.r = nr;
            this.c = nc;
            fishMap[nr][nc].num = 's';
            this.dir = fishMap[nr][nc].dir;
        }
    }

    static void moveAllFish(Fish[][] fishMap, Fish[] fishArr) {
        for (int i = 0; i < 16; ++i)
            if (fishArr[i] != null && 0 < fishArr[i].num && fishArr[i].num < 's')
                fishArr[i].move(fishMap);
    }
    static void copyFishMapAndArr(Fish[][] originalMap, Fish[] originalArr, Fish[][] fishMapCopy, Fish[] fishArrCopy) {
        for (int i =0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                fishMapCopy[i][j] = originalMap[i][j].copy(originalMap[i][j]);
                if (0 < fishMapCopy[i][j].num && fishMapCopy[i][j].num < 's')
                    fishArrCopy[fishMapCopy[i][j].num - 1] = fishMapCopy[i][j];
            }
        }
    }

    static int recursive(Fish[][] fishMap, Fish[] fishArr, TeenShark shark, int nr, int nc) {
        Fish[][] fishMapCopy = new Fish[4][4];
        Fish[] fishArrCopy = new Fish[16];
        copyFishMapAndArr(fishMap, fishArr, fishMapCopy, fishArrCopy);

        TeenShark sharkCopy = new TeenShark(shark.r, shark.c, shark.dir, shark.eatenFishSum);
        sharkCopy.move(fishMapCopy, nr, nc);
        moveAllFish(fishMapCopy, fishArrCopy);

        int maxEatenFish = sharkCopy.eatenFishSum;
        while (true) {
            nr += dirR[sharkCopy.dir];
            nc += dirC[sharkCopy.dir];
            if (nr < 0 || nr >= 4 || nc < 0 || nc >= 4)
                break;
            if (fishMapCopy[nr][nc].num == 0)
                continue;

            int tmpEatenFishSum = recursive(fishMapCopy, fishArrCopy, sharkCopy, nr, nc);
            maxEatenFish = Math.max(maxEatenFish, tmpEatenFishSum);
        }
        return maxEatenFish;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Fish[][] fishMap = new Fish[4][4];
        Fish[] fishArr = new Fish[16];

        // input
        for (int i =0; i < 4; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; ++j) {
                int num = Integer.parseInt(st.nextToken());
                int dir = Integer.parseInt(st.nextToken());
                fishArr[num - 1] = fishMap[i][j] = new Fish(i, j, num, dir);
            }
        }

        // initialize
        TeenShark shark = new TeenShark();

        System.out.println(recursive(fishMap, fishArr, shark, 0, 0));
    }
}