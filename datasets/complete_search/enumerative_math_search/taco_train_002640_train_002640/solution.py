(n, k, A) = map(int, input().rstrip().split())
senators = []
mx_bribe = 0
for i in range(n):
	(lvl, loy) = map(int, input().rstrip().split())
	senators.append((lvl, loy))
	mx_bribe += (100 - loy) // 10
bribe = [0] * n

def calc(votes):
	(bsum, cnt, p) = (0, 0, 1.0)
	for (i, s) in enumerate(senators):
		if votes & 1 << i:
			p *= (s[1] + bribe[i]) / 100
			cnt += 1
		else:
			p *= (100 - s[1] - bribe[i]) / 100
			bsum += s[0]
	if cnt > n / 2:
		return p
	else:
		return p * A / (A + bsum)

def dfs(cur, rk):
	if cur >= n:
		if rk > 0:
			return 0.0
		sm = 0.0
		for i in range(1 << n):
			sm += calc(i)
		return sm
	mx = 0.0
	for i in range(rk + 1):
		if i * 10 + senators[cur][1] > 100:
			break
		bribe[cur] = i * 10
		tmp = dfs(cur + 1, rk - i)
		mx = max(tmp, mx)
	return mx
print(dfs(0, min(k, mx_bribe)))
