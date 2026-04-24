from itertools import permutations
(n, k) = map(int, input().split())
print(min((max(k) - min(k) for k in zip(*[[int(''.join(j)) for j in permutations(input())] for i in range(n)]))))
