#include <iostream>
#include <vector>

// https://codeforces.com/contest/1676/problem/H2

//该函数用于计算两个有序数组的逆序对数目
//
//首先,a[left...mid]和a[mid+1...right]都是有序的
//然后,我们用两个指针i和j分别指向这两个数组的首元素
//如果a[i]<a[j],那么a[i]就不会和a[j]构成逆序对
//如果a[i]>=a[j],那么a[i]就会和a[j...mid]构成逆序对
//因为a[j...mid]都是大于等于a[j]的,所以a[i]也会大于等于a[j]
//所以a[i]也会大于等于a[j...mid]中的每一个元素,所以会构成逆序对
//
//@param a: 待计算的数组
//@param left: 数组的左边界
//@param mid: 数组的中间位置
//@param right: 数组的右边界
//@return: 逆序对的数目
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

/* 该函数用来计算数组a[left...right]中的逆序对数目
 *
 * @param a: 待计算的数组
 * @param left: 数组的左边界
 * @param right: 数组的右边界
 * @return: 逆序对的数目
 */
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