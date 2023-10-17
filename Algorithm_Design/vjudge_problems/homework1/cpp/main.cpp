#include <iostream>
#include <cmath>
#include <unordered_map>

long long countTrailingOnes(long long n) {
    int count = 0;
    while (n & 1) {
        count++;
        n >>= 1;
    }
    return count;
}

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