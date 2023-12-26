#include <vector>
#include <iostream>
#include <ranges>

using namespace std;

int main() {
    int k;
    cin >> k;
    while (k--) {
        int n;
        cin >> n;

        vector<int> a(n + 1), b(n + 1);
        for (int i : std::views::iota(1, n + 1)) {
            cin >> a[i];
        }
        for (int i : std::views::iota(1, n + 1)) {
            cin >> b[i];
        }

        for (int i : std::views::iota(2, n + 1)) {
            b[i] = max(b[i], b[i - 1]);
        }

        int min_index = INT_MAX;
        for (int i : std::views::iota(1, n + 1)) {
            int t = upper_bound(b.begin() + 1, b.end(), a[i]) - b.begin();
            min_index = min(min_index, i + t - 2);
        }

        cout << min_index << endl;
    }
    return 0;
}
