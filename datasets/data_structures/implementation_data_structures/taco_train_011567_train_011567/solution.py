n = int(input())
p = list(zip(map(int, input().split()), map(int, input().split()), map(int, input().split())))
m = int(input())
p.sort()
(t, ans) = ([0, 0, 0, 0], [])
for c in map(int, input().split()):
	while t[c] < n and (p[t[c]] == None or c not in p[t[c]][1:]):
		t[c] += 1
	if t[c] == n:
		ans.append(-1)
	else:
		ans.append(p[t[c]][0])
		p[t[c]] = None
print(*ans)
