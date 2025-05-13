#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->ios::sync_with_stdio(0);
    
    int T; 
    cin >> T;
    cin.ignore();
    while (T--) {
        string totalSounds;
        getline(std::cin, totalSounds);

        unordered_map<string, string> map;
        while (1) {
            string animal, goes, sound;
            cin >> animal >> goes >> sound;

            if (goes == "does") {
                string tmp;
                getline(std::cin, tmp);
                break;
            }

            map[sound] = animal;
        }

        stringstream ss(totalSounds);
        string token;
        string ans;
        while (ss >> token) {
            if (map.find(token) != map.end()) {
                continue;
            }

            ans = ans + token + ' ';
        }
        cout << ans << '\n';
    }

    return 0;
}