for _ in range(int(input())):
	n = int(input())
	fi = list(map(int, input().split()))
	ci = list(map(int, input().split()))
	fc = list(zip(fi, ci))
	fc.sort(key=lambda e: e[1])
	ans = 0
	for (f, c) in fc:
		cnt = min(f, n)
		n -= cnt
		ans += cnt * c
	print(ans)
