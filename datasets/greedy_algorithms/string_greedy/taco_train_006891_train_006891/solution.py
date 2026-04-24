n = int(input()) // 2
a = sorted([input() for i in range(n * 2)], reverse=1)
d = input()
L = sum((len(i) for i in a)) // n
ans = []
for i in range(n):
	x = a.pop()
	for y in a[::-1]:
		if len(x) + len(y) == L:
			ans.append(min(x + d + y, y + d + x))
			a.remove(y)
			break
print('\n'.join(sorted(ans)))
