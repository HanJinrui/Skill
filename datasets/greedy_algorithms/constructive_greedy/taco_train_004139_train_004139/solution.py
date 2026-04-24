from collections import Counter
for _ in range(int(input())):
	n = int(input())
	A = list(map(int, input().split()))
	if max(Counter(A).values()) > (n + 1) // 2:
		print(-1)
	else:
		k = 0
		cnt = Counter()
		cnt[A[0]] += 1
		cnt[A[-1]] += 1
		for i in range(n - 1):
			if A[i] == A[i + 1]:
				cnt[A[i]] += 2
				k += 1
		print(k + max(0, max(cnt.values()) - (k + 2)))
