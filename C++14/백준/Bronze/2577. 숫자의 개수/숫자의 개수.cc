#include <bits/stdc++.h>
using namespace std;

int arr[10];

int main() {
    cin.tie(0)->ios::sync_with_stdio(0);
    
    int a, b, c; cin >> a >> b >> c;

    int sum = a * b * c;
    while (sum) {
        arr[sum%10]++;
        sum /= 10;
    }

    for(int el : arr) {
        cout << el << '\n';
    }

    return 0;
}