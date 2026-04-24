from collections import Counter
for _ in range(int(input())):
	input()
	ml = list(Counter([int(s) for s in input().split()]).values())
	k = ml.index(max(ml))
	ml.append(ml[k] // 2 + ml[k] % 2)
	ml[k] //= 2
	print(max(ml))
