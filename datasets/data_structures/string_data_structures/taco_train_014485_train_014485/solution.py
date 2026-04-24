from collections import Counter
for _ in range(int(input())):
	(s, t) = input().split()
	print('YES' if (set(s) == set(t)) == (Counter(s) == Counter(t)) else 'NO')
