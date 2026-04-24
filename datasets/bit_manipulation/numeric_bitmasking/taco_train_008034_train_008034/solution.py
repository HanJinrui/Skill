def solver():
	T = int(input())
	for _ in range(T):
		ans = 0
		n = int(input())
		arr = [int(x) for x in input().split()]
		for i in range(1, len(arr)):
			arr[i] = arr[i] ^ arr[i - 1]
		for i in range(32, -1, -1):
			t = 1 << i
			cnt = 0
			for e in arr:
				if e & t != 0:
					cnt += 1
			ans += cnt * (n - cnt + 1) * t
		print(ans)
solver()
