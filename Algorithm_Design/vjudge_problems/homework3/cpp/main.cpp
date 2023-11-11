#include <iostream>
#include <vector>

// https://codeforces.com/contest/1676/problem/H2

long long merge(std::vector<int> &a, int left, int mid, int right) {
    int i = left, j = mid + 1, k = 0;
    std::vector<int> temp(right - left + 1);
    long long count = 0;
    while (i <= mid && j <= right) {
        if (a[i] < a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
            count += mid - i + 1;
        }
    }
    std::move(a.begin() + i, a.begin() + mid + 1, temp.begin() + k);
    std::move(a.begin() + j, a.begin() + right + 1, temp.begin() + k);
    std::move(temp.begin(), temp.end(), a.begin() + left);
    return count;
}

long long countInversions(std::vector<int> &a, int left, int right) {
    long long count = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;
        count += countInversions(a, left, mid);
        count += countInversions(a, mid + 1, right);
        count += merge(a, left, mid, right);
    }
    return count;
}

int main() {
    int t, n;
    std::cin >> t;
    while (t--) {
        std::cin >> n;
        std::vector<int> a(n);
        for (auto &i: a) {
            std::cin >> i;
        }
        std::cout << countInversions(a, 0, n - 1) << "\n";
    }
    return 0;
}