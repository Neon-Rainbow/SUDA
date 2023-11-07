#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

// 优化C++输入输出性能
void enableFastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
}

/**
 * 计算并存储所有可能的子序列和。
 * @param left 子序列的左边界。
 * @param right 子序列的右边界。
 * @param elements 排序后的元素数组。
 * @param subsequenceSums 存储子序列和的集合。
 * @param cumulativeSums 累计和数组，用于快速计算子序列和。
 */
void calculateSubsequenceSums(int left, int right, const vector<int>& elements, unordered_set<long long>& subsequenceSums, const vector<long long>& cumulativeSums) {
    auto middle = static_cast<int>(upper_bound(elements.begin() + left, elements.begin() + right + 1, (elements[left] + elements[right]) / 2) - elements.begin());
    subsequenceSums.emplace(cumulativeSums[right + 1] - cumulativeSums[left]);
    if (middle == right + 1 || middle == left) {
        return;
    }
    calculateSubsequenceSums(middle, right, elements, subsequenceSums, cumulativeSums);
    calculateSubsequenceSums(left, middle - 1, elements, subsequenceSums, cumulativeSums);
}

int main() {
    enableFastIO();
    int numTests, numElements, numQueries;
    cin >> numTests;
    while (numTests--) {
        cin >> numElements >> numQueries;
        vector<int> elements(numElements);
        vector<long long> cumulativeSums(numElements + 1);
        for (auto& element : elements) {
            cin >> element;
        }
        sort(elements.begin(), elements.end());
        cumulativeSums[0] = 0;
        for (size_t i = 0; i < elements.size(); ++i) {
            cumulativeSums[i + 1] = elements[i] + cumulativeSums[i];
        }
        unordered_set<long long> subsequenceSums;
        calculateSubsequenceSums(0, numElements - 1, elements, subsequenceSums, cumulativeSums);
        while (numQueries--) {
            int queryValue;
            cin >> queryValue;
            // 如果子序列和存在于集合中，则输出"Yes"，否则输出"No"
            cout << (subsequenceSums.count(queryValue) ? "Yes\n" : "No\n");
        }
        subsequenceSums.clear();
    }
}
