// Time Complexity: O(log n)
// Auxiliary Space: O(1)

int mySqrt(int x) {
    int l = 0;
    int r = x;
    int m;

    while (l <= r) {
        m = l + (r - l) / 2;
        
        long sqr = pow(m, 2);

        if (sqr > x) {
            r = m - 1;
        } else if (sqr < x) {
            l = m + 1;
        } else {
            return m;
        }
    }

    return r;
}