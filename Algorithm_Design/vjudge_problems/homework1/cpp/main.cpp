#include <iostream>
#include <cmath>
#include <unordered_map>


/**
 * @brief Count the number of trailing zeros in the binary representation of a number.
 *
 * @param num The number to be analyzed.
 * @return The count of trailing zeros in the binary representation of num.
 */
long long countTrailingOnes(long long num) {
    return num == 0 ? 0 : __builtin_ctzll(~num);
}

/**
 * @brief Get the bit value at the specified position from the left in the binary representation of a number.
 *
 * @param binary The number to be analyzed.
 * @param n The position from the left in the binary representation.
 * @param cache A cache to store previously computed results to avoid redundant computations.
 * @return The bit value (0 or 1) at the specified position.
 */
long long getNthBitFromLeft(long long binary, long long n, std::unordered_map<long long, long long> &cache) {
    int totalBits = std::log2(binary) + 1;
    int positionFromRight = totalBits - n - 1;
    if (cache.find(n) != cache.end()) {
        return cache[n];
    }
    long long temp = (binary >> positionFromRight) & 1;
    cache[n] = temp;
    return temp;
}
/**
 * @brief Calculate the value at a specific index in the transformed sequence.
 *
 * @param num The initial number.
 * @param index The index in the sequence.
 * @param cache A cache to store previously computed results to avoid redundant computations.
 * @return The value (0 or 1) at the specified index in the transformed sequence.
 */

long long cal(long long num, long long index, std::unordered_map<long long, long long> &cache) {
    if(index % 2 == 0) {
        return 1;
    }
    return getNthBitFromLeft(num, countTrailingOnes(index), cache);
}


int main() {
    std::unordered_map<long long, long long> cache;
    long long num, l, r;
    std::cin >> num >> l >> r;
    long long count = 0;
    long long MAX = std::pow(2, int(std::log2(num) + 1)) - 1;
    r = std::min(r, MAX);
    for (long long i = l - 1; i < r; i++) {
        count += cal(num, i, cache);
    }
    std::cout << count << std::endl;
    return 0;
}