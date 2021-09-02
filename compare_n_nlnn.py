from math import log2


n = 100
for k in range(1, 100):
    print(k, n*k, n*log2(n/k))