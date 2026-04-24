for t in range(int(input())):
	n = int(input())
	a = [int(i) for i in input().split()]
	store = {0: 0}
	s = 0
	for i in range(n):
		s = (s + a[i]) % n
		if s in store:
			ans = range(store[s] + 1, i + 2)
			break
		store[s] = i + 1
	print(len(ans))
	print(*ans)
