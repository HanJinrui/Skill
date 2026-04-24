T = int(input())
for _ in range(T):
	n = int(input())
	a = list(map(int, input().split()))
	if len(a) != len({*a}):
		print('NO')
		continue
	ans = True
	for i in range(2, 55):
		cnt = [0] * i
		for x in a:
			cnt[x % i] += 1
		if min(cnt) >= 2:
			ans = False
	print('YES' if ans else 'NO')
