# Matrix multiplication

import sys;

def MatrixMul(m, i, j):
    if i == j:
        return 0

    _min = sys.maxsize

    for k in range(i, j):

        count = (MatrixMul(m, i, k)
                 + MatrixMul(m, k + 1, j)
                 + m[i - 1] * m[k] * m[j])

        if count < _min:
            _min = count;

    return _min;


arr = [1, 2, 3, 4, 2];
n = len(arr);

print("Minimum number of multiplication is ",
      MatrixMul(arr, 1, n - 1));