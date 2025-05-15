#include <bits/stdc++.h>
using namespace std;

void getAns() {
    // S점수, T점수, 킥카운트
    int S, T; cin >> S >> T;
    int kickCount = 0;

    // [S점수][T점수]
    bool visitedScore[1000][1000] = {};

    queue<tuple<int, int, int>> q;
    q.push({S, T, 0});
    
    while (!q.empty()) {
        int curS = get<0>(q.front());
        int curT = get<1>(q.front());
        int cnt = get<2>(q.front());
        q.pop();

        // 이미 방문한 케이스
        if (visitedScore[curS][curT]) {
            continue;
        }

        // 새 케이스
        if (curS == curT) {
            cout << cnt << '\n';
            return;
        }
        visitedScore[curS][curT] = true;
        q.push({curS+1, curT, cnt+1});
        if (curS*2 <= curT+3) {
            q.push({curS*2, curT+3, cnt+1});
        }
    }
}

int main() {
    cin.tie(0)->ios::sync_with_stdio(0);
    
    int C; cin >> C;

    while (C--) {
        getAns();
    }

    return 0;
}
