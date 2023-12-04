#include <iostream>
#include <bitset>

constexpr int MAX_LENGTH = 200001;

int main() {
    int t;
    std::cin >> t;
    while(t--) {
        int n;
        std::cin >> n;
        std::bitset<MAX_LENGTH>btst;
        btst.reset();
        btst.set(0);
        auto dp = [&btst, &n] {
            int x;
            for(int i = 1; i <= n; ++i) {
                std::cin >> x;
                if(i + x < MAX_LENGTH) {
                    btst[i + x] = btst[i - 1] | btst[i + x];
                }
                if(i - x - 1 >= 0) {
                    btst[i] = btst[i - x - 1] | btst[i];
                }
            }
            return btst[n]? "YES" : "NO";
        };
        std::cout << dp() << std::endl;
    }
}
