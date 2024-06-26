## 算法复杂度

|            | InsertionSort   | ShellSort                 | SelectSort      | BubbleSort      | QuickSort                                   | HeapSort          | MergeSort         |
| ---------- | --------------- | ------------------------- | --------------- | --------------- | ------------------------------------------- | ----------------- | ----------------- |
| 时间复杂度 | $T(n) = O(n^2)$ | $T(n) = O(n^\frac{3}{2})$ | $T(n) = O(n^2)$ | $T(n) = O(n^2)$ | 平均:$T(n) = O(nlogn)$ 最差:$T(n) = O(n^2)$ | $T(n) = O(nlogn)$ | $T(n) = O(nlogn)$ |
| 空间复杂度 | $S(n) = O(1)$   | $S(n) = O(1)$             | $S(n) = O(1)$   | $S(n) = O(1)$   | $S(n) = O(logn)$                            | $S(n) = O(1)$     | $S(n) = O(n)$     |
|            |                 |                           |                 |                 |                                             |                   |                   |

## 运行时间

正序:

|       | InsertionSort | ShellSort | SelectSort | BubbleSort | QuickSort | HeapSort | MergeSort |
| ----- | ------------- | --------- | ---------- | ---------- | --------- | -------- | --------- |
| 1000  | 2             | 1         | 3          | 1          | 2         | 1        | 1         |
| 3000  | 3             | 2         | 8          | 3          | 7         | 2        | 2         |
| 10000 | 3             | 3         | 69         | 3          | 51        | 3        | 4         |

逆序:

|       | InsertionSort | ShellSort | SelectSort | BubbleSort | QuickSort | HeapSort | MergeSort |
| ----- | ------------- | --------- | ---------- | ---------- | --------- | -------- | --------- |
| 1000  | 4             | 2         | 2          | 5          | 1         | 1        | 1         |
| 3000  | 12            | 2         | 8          | 28         | 8         | 3        | 2         |
| 10000 | 100           | 3         | 72         | 288        | 50        | 5        | 3         |

随机:

|       | InsertionSort | ShellSort | SelectSort | BubbleSort | QuickSort | HeapSort | MergeSort |
| ----- | ------------- | --------- | ---------- | ---------- | --------- | -------- | --------- |
| 1000  | 3             | 2         | 2          | 4          | 2         | 2        | 2         |
| 3000  | 5             | 1         | 8          | 18         | 1         | 2        | 1         |
| 10000 | 43            | 6         | 71         | 189        | 3         | 2        | 3         |
