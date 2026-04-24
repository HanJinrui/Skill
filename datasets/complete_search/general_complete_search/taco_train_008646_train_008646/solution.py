prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51]
(n, m) = map(int, input().split())
print('YNEOS'[prime[prime.index(n) + 1] != m::2])
