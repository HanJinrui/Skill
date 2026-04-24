from collections import *
I = input
for _ in [0] * int(I()):
	(n, k) = map(int, I().split())
	s = I()
	s += s[::-1]
	print(n - sum((max(Counter(s[i::k]).values()) for i in range(k))) // 2)
