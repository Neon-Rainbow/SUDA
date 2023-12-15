#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int k;
    std::cin >> k;
    while (k--) {
        int min_distance = INT_MAX;
        int n;
        std::cin >> n;
        std::vector<int> a(n), b(n);
        for (int i = 0; i < n; i++) {
            std::cin >> a[i];
        }
        for (int i = 0; i < n; i++) {
            std::cin >> b[i];
        }
        for (int i = 1; i < n; i++) {
            b[i] = std::max(b[i], b[i - 1]);
        }
        for (int i = 0; i < n; ++i) {
            int t = std::upper_bound(b.begin(), b.end(), a[i]) - b.begin();
            min_distance = std::min(min_distance, i + t - 1);
        }
        std::cout << min_distance << std::endl;
    }
    return 0;
}
