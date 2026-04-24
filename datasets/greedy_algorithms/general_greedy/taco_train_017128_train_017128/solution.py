input()
t = [*map(int, input())]
f = (0, *input().split())
c = 0
a = 0
for b in t:
	n = int(f[b])
	if n > b or (n == b and c):
		c = 1
		t[a] = n
	elif c:
		break
	a += 1
print(*t, sep='')
