for _ in range(int(input())):
	n = int(input())
	a = sorted(zip(map(int, input().split()), map(int, input().split())), reverse=True)
	ans = 1
	mx = a[0][1]
	for (i, j) in a:
		if j > mx:
			ans += 1
			mx = j
	print(ans)
