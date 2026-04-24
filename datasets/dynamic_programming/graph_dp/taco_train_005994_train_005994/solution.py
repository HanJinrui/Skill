R = lambda : map(int, input().split())
(n, k) = R()
s = input()
p = [s]
ans = 0
d = set()
while p:
	q = p.pop(0)
	if q not in d:
		k -= 1
		ans += n - len(q)
		if k == 0:
			print(ans)
			quit()
		d.add(q)
		for i in range(len(q)):
			t = q[:i] + q[i + 1:]
			if t not in p:
				p.append(t)
print(-1)
