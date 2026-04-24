from collections import Counter
for _ in range(int(input())):
	k = input()
	r = Counter(k)
	if len(r) == 1:
		print(len(k))
	elif r['a'] % 2 == r['b'] % 2 == r['c'] % 2:
		print(2)
	else:
		print(1)
