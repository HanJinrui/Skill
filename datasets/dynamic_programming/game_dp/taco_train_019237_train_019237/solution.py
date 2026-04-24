sg = [0] * 1156
sg[0] = sg[1] = 0
vis = [False] * 1156
for i in range(2, 1156):
	for j in range(0, i - 1):
		vis[sg[j] ^ sg[i - j - 2]] = True
	for j in range(0, 1156):
		if not vis[j]:
			sg[i] = j
			break
	for j in range(0, i - 2):
		vis[sg[j] ^ sg[i - j - 2]] = False
for tc in range(int(input())):
	N = int(input())
	S = input()
	(R, B) = (S.count('R'), S.count('B'))
	if R > B:
		print('Alice')
		continue
	if R < B:
		print('Bob')
		continue
	(l, r, ans) = (0, 0, 0)
	while l < N:
		r = l + 1
		while r < N and S[r - 1] != S[r]:
			r += 1
		ans ^= sg[r - l] if r - l < 1156 else sg[1122 + (r - l) % 34]
		l = r
	print('Alice' if ans != 0 else 'Bob')
