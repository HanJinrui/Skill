a = [0]
for x in input().split('o'):
	a += (a[-1] + max(0, len(x) - 1),)
print(sum((x * (a[-1] - x) for x in a)))
