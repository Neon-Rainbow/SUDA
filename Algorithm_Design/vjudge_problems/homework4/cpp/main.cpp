#include <iostream>
#include <string>


int CalculateDifferentChar(const std::string::iterator&left,
                           const std::string::iterator&right,
                           const char&target) {
    int ans = 0;
    for (auto iter = left; iter != right + 1; ++iter) {
        if (*iter != target) {
            ans++;
        }
    }
    return ans;
}

int CalculateMinimumChangesToMakeStringAGood(const std::string::iterator&left,
                                             const std::string::iterator&right,
                                             const char&target) {
    if (std::distance(left, right) == 0) {
        return CalculateDifferentChar(left, right, target);
    }
    const auto mid = left + (right - left) / 2;
    return std::min(
        CalculateMinimumChangesToMakeStringAGood(left, mid, static_cast<char>(target + 1)) + CalculateDifferentChar(
            mid + 1, right, target),
        CalculateMinimumChangesToMakeStringAGood(mid + 1, right, static_cast<char>(target + 1)) +
        CalculateDifferentChar(
            left, mid, target)
    );
}


int main() {
    int t;
    std::cin >> t;
    std::string s;
    while (t--) {
        int length;
        std::cin >> length;
        std::cin >> s;
        std::cout << CalculateMinimumChangesToMakeStringAGood(s.begin(), s.end() - 1, 'a') << std::endl;
    }
    return 0;
}
