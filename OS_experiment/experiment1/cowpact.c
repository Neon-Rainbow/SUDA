#include <stdio.h>

int main() {
    int c, n = 0;  // 'n'用于追踪连续换行符的数量。
    const int kMaxNewlines = 1;  // 允许的连续换行符的最大数量常量。

    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            ++n;  // 增加换行符计数器。
        } else {
            n = 0;  // 对于非换行符字符，重置计数器。
        }

        if (n <= kMaxNewlines) {
            putchar(c);  // 如果在换行符限制内，则输出字符。
        }
        // 当'n'超过'kMaxNewlines'时，我们不需要else块，因为我们什么也不做。
    }

    return 0;
}
