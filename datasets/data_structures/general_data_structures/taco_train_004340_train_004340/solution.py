import heapq, sys
q = []
c = 0
n = int(input())
s = input()
a = list(map(int, input().split()))
l = [i - 1 for i in range(n)]
r = [i + 1 for i in range(n)]
for i in range(n - 1):
	if s[i] != s[i + 1]:
		heapq.heappush(q, (abs(a[i] - a[i + 1]), i, i + 1))
		c += 1
ans = []
while c > 0:
	(t, i, j) = heapq.heappop(q)
	c -= 1
	if r[i] == -1 or r[j] == -1:
		continue
	ans.append('%d %d' % (i + 1, j + 1))
	(u, v) = (l[i], r[j])
	r[i] = r[j] = -1
	if u >= 0:
		r[u] = v
	if v < n:
		l[v] = u
	if u >= 0 and v < n and (s[u] != s[v]):
		heapq.heappush(q, (abs(a[u] - a[v]), u, v))
		c += 1
sys.stdout.write(str(len(ans)) + '\n' + '\n'.join(ans) + '\n')
