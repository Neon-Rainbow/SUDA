#include <iostream>
#include <vector>

void solve() {
    int n;
    std::cin >> n;

    std::vector<int> a(n);
    std::vector<int> b(n);
    std::vector<int> c(n);

    for(auto &i:c) {
        std::cin >> i;
    }

    for(auto &i:a) {
        std::cin >> i;
    }

    for(auto &i:b) {
        std::cin >> i;
    }

    long long ans{0};
    long long curr{0};

    for(int i = 1; i < n; i++) {
        const auto distance{std::abs(a[i] - b[i])};
        const auto temp{curr + c[i - 1] - distance - 1};
        if(distance == 0) {
            curr = 2;
        }else {
            curr = i == 1 || temp < distance ? distance : temp;
            curr += 2;
        }
        ans = std::max(ans , curr + c[i] - 1);
    }
    std::cout << ans << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
}
