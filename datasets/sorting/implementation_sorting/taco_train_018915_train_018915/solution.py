from collections import Counter
a = int(input())
b = Counter(map(int, input().split()))
z = sorted(((b[j], b[k], i) for (i, j, k) in zip(range(1, int(input()) + 1), map(int, input().split()), map(int, input().split()))))[::-1]
print(z[0][2])
