#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void solve(const int &n, int a[], int b[], int c[]) {
    long long ans = 0, curr = 0;
    for (int i = 1; i < n; i++) {
        const long long distance = llabs(a[i] - b[i]);
        const long long temp = curr + c[i - 1] - distance - 1;
        if (distance == 0) {
            curr = 2;
        } else {
            curr = (i == 1 || temp < distance) ? distance : temp;
            curr += 2;
        }
        if (curr + c[i] - 1 > ans) {
            ans = curr + c[i] - 1;
        }
    }
    printf("%lld\n", ans);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int *a = (int*)malloc(n * sizeof(int));
        int *b = (int*)malloc(n * sizeof(int));
        int *c = (int*)malloc(n * sizeof(int));

        for (int i = 0; i < n; i++) {
            scanf("%d", &c[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &b[i]);
        }

        solve(n, a, b, c);

        free(a);
        free(b);
        free(c);
    }
    return 0;
}
