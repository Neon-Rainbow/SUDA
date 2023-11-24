#include <iostream>
#include <vector>

int solve(const std::vector<int> &v) {
    const int n = v.size() - 1;
    std::vector<int>dp(n + 2, INT_MAX/2);
    dp[n + 1] = 0;
    for(int i = n; i >= 1; i--) {
        dp[i] = std::min(dp[i], dp[i + 1] + 1);
        if(i + v[i] <= n) {
            dp[i] = std::min(dp[i], dp[i + v[i] + 1]);
        }
    }
    return *(dp.begin() + 1);
}


int main() {
    int t;
    std::cin >> t;
    while(t--) {
        int n;
        std::cin >> n;
        std::vector<int> v(n + 1);
        for(auto iter = v.begin() + 1; iter != v.end(); iter++) {
            std::cin >> *iter;
        }
        std::cout << solve(v) << "\n";
    }

}
