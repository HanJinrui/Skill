for cs in range(int(input())):
	n = int(input())
	cnt = [[] for _ in range(4)]
	S = set()
	rev_hash = []
	for i in range(n):
		s = input()
		cnt[int(s[0]) * 2 + int(s[-1])].append(i)
		S.add(hash(s))
		rev_hash.append(hash(s[::-1]))
	if len(cnt[0] + cnt[3]) == n and len(cnt[0]) > 0 and (len(cnt[3]) > 0):
		print(-1)
	else:
		diff = len(cnt[1]) - len(cnt[2])
		if diff < 0:
			(cnt[1], cnt[2]) = (cnt[2], cnt[1])
			diff = abs(diff)
		diff //= 2
		ans = []
		for i in cnt[1]:
			if diff == 0:
				break
			if rev_hash[i] not in S:
				diff -= 1
				ans.append(i + 1)
		if diff != 0:
			print(-1)
		else:
			print(len(ans))
			print(*ans)
