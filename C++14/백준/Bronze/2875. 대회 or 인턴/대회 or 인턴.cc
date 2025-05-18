#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->ios::sync_with_stdio(0);
    
    // 여자, 남자, 인턴쉽
    int N, M, K;
    cin >> N >> M >> K;

    // 일단 남녀 수로 구할 수 있는 최대 팀 수 구하기
    int teamCnt = 0;
    while (N >= 2 && M >= 1) {
        N -= 2;
        M--;
        teamCnt++;
    }

    // 인턴십 인원 빼기
    K = max(K - N - M, 0);
    while (K) {
        K = max(K-3, 0);
        teamCnt--;
    }

    cout << teamCnt;
    
    return 0;
}