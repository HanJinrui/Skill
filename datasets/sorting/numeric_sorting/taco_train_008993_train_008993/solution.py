from collections import Counter
(n, k) = map(int, input().split())
for x in range(1, k + 2):
	print('?', *(y for y in range(1, k + 2) if y != x))
cnt = Counter((int(input().split()[1]) for _ in range(k + 1)))
print('!', cnt[max(cnt.keys())])
