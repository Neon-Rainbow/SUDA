#include <iostream>
#include <vector>

void solve() {
    int n;
    std::cin >> n;

    std::vector<int> a(n);
    std::vector<int> b(n);
    std::vector<int> c(n);

    for(int i = 0; i < n; i++) {
        std::cin >> c[i];
    }

    for(int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    for(int i = 0; i < n; i++) {
        std::cin >> b[i];
    }

    long long ans{0};
    long long curr{0};

    for(int i = 1; i < n; i++) {
        const auto distance{std::abs(a[i] - b[i])};
        if(distance == 0) {
            curr = 2;
            ans = std::max(ans , curr + c[i] - 1);
            continue;
        }
        if(i == 1 || curr + c[i - 1] - 2 * distance - 1 < 0) {
            curr = distance;
        }else {
            curr += c[i - 1] - distance - 1;
        }
        curr += 2;
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
