#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->ios::sync_with_stdio(0);
    
    long long N;
    cin >> N;

    // N이 2진수로 몇자리수인지 구하기
    long long tmp = N;
    int cnt = 0;
    while (tmp) {
        tmp /= 2;
        cnt++;
    }

    // 그 자리수에서 나올 수 있는 최대 수
    long long mask = 1;
    for (int i = 1; i < cnt; i++)  {
        mask = mask * 2 + 1;
    }

    // 그 수를 N과 xor
    long long theNumber = N ^ mask;

    if (theNumber == 0) {
        cout << 1 << '\n';
        cout << N;
    } else {
        cout << 2 << '\n';
        cout << theNumber << '\n';
        cout << N << '\n';
    }
    
    return 0;
}